from flask import Flask, render_template, request
from serpapi import GoogleSearch
from bs4 import BeautifulSoup
from groq import Groq
import requests
import re

app = Flask(__name__)

SERP_API_KEY = ""
GROQ_API_KEY = ""

client = Groq(api_key= GROQ_API_KEY)


def detect_stage(text):

    stages = [
        "pre-seed",
        "seed",
        "angel",
        "series a",
        "series b",
        "series c",
        "series d",
        "ipo",
        "bootstrapped"
    ]

    for stage in stages:
        if stage in text.lower():
            return stage.title()

    return "Not Mentioned"


def summarize(text):

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role":"user",
                    "content":
                    f"""
Summarize this startup.
{text}
Return

Startup

Industry

Products

Country

Summary

"""
                }
            ]
        )

        return response.choices[0].message.content

    except:

        return "Summary unavailable."


def scrape_website(url):

    try:

        headers = {
            "User-Agent":"Mozilla/5.0"
        }
        

        response = requests.get(url,headers=headers,timeout=10)

        soup = BeautifulSoup(response.text,"html.parser")

        title = soup.title.text.strip() if soup.title else "Unknown"

        description = ""

        tag = soup.find("meta",attrs={"name":"description"})

        if tag:
            description = tag.get("content","")

        text = soup.get_text(" ",strip=True)


        year_founded = ""
        year_founded = re.findall(r"20\d\d|19\d\d", text)
        
        
        careers_page = ""
        for a in soup.find_all("a", href=True):
            href = a["href"].lower()

            if "career" in href or "jobs" in href:
                careers_page = href

        contact_page = ""
        for a in soup.find_all("a", href=True):
            href = a["href"].lower()

            if "contact" in href:
                contact_page = href


        email = ""

        email_match = re.search(r'[\w\.-]+@[\w\.-]+',text)

        if email_match:
            email = email_match.group()

        phone = ""

        phone_match = re.search(r'\+?\d[\d\s-]{8,15}',text)

        if phone_match:
            phone = phone_match.group()

        linkedin = ""

        twitter = ""

        for link in soup.find_all("a",href=True):

            href = link["href"]

            if "linkedin.com" in href:
                linkedin = href

            if "twitter.com" in href or "x.com" in href:
                twitter = href

        return {

            "startup_name":title,

            "website":url,

            "year_founded": year_founded,

            "description":description,

            "summary":summarize(text[:6000]),

            "funding_stage":detect_stage(text),

            "email":email,

            "phone":phone,

            "linkedin":linkedin,

            "twitter":twitter,

            "careers_page": careers_page,

            "contact_page": contact_page
        }

    except Exception as e:
        print("ERROR:", e)
        return None


@app.route("/")

def home():

    return render_template("index.html")


@app.route("/scraper",methods=["POST"])

def scraper():
    
    print("SCRAPER ROUTE CALLED")
    query = request.form.get("query")
    print(query)
    params = {

        "engine":"google",

        "q":query,

        "api_key":SERP_API_KEY

    }

    search = GoogleSearch(params)

    results = search.get_dict()

    startups = []

    for result in results.get("organic_results",[])[:5]:
        
        print(result)
        url = result.get("link")
        print("URL =", url)
        if not url:
            continue

        data = scrape_website(url)

        if data:

            startups.append(data)
    print(startups)

    return render_template(

        "index.html",

        startups=startups,

        query=query

    )


if __name__=="__main__":

    app.run(debug=True, port=5003)
