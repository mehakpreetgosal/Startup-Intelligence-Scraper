
document.addEventListener("DOMContentLoaded", () => {

    console.log("Startup Intelligence Scraper Loaded");

    // -----------------------------
    // Smooth Scrolling
    // -----------------------------
    document.querySelectorAll('a[href^="#"]').forEach(link => {

        link.addEventListener("click", function (e) {

            e.preventDefault();

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {

                target.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });

    // -----------------------------
    // Navbar Shadow
    // -----------------------------
    const navbar = document.querySelector(".navbar");

    if (navbar) {

        window.addEventListener("scroll", () => {

            if (window.scrollY > 50) {

                navbar.style.boxShadow =
                    "0 5px 15px rgba(0,0,0,0.25)";

            } else {

                navbar.style.boxShadow = "none";

            }

        });

    }

    // -----------------------------
    // Search Form
    // -----------------------------
    const form = document.querySelector(".scraper-input-section form");

    if (form) {

        form.addEventListener("submit", function (event) {

            const queryInput = form.querySelector('input[name="query"]');

            const button = form.querySelector("button");

            if (!queryInput) {

                return;

            }

            const query = queryInput.value.trim();

            if (query === "") {

                event.preventDefault();

                alert("Please enter an industry or startup keyword.");

                return;

            }

            button.disabled = true;

            button.innerHTML = "Searching...";

        });

    }

    // -----------------------------
    // Button Animation
    // -----------------------------
    document.querySelectorAll(".btn").forEach(btn => {

        btn.addEventListener("mouseenter", () => {

            btn.style.transform = "scale(1.05)";

        });

        btn.addEventListener("mouseleave", () => {

            btn.style.transform = "scale(1)";

        });

    });

    // -----------------------------
    // Fade-in Animation
    // -----------------------------
    const animatedItems = document.querySelectorAll(

        ".feature, .scraper-section, .scraper-input-section, .result-card"

    );

    if ("IntersectionObserver" in window) {

        const observer = new IntersectionObserver((entries) => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    entry.target.style.opacity = "1";

                    entry.target.style.transform = "translateY(0)";

                }

            });

        }, {

            threshold: 0.2

        });

        animatedItems.forEach(item => {

            item.style.opacity = "0";

            item.style.transform = "translateY(40px)";

            item.style.transition = "all 0.8s ease";

            observer.observe(item);

        });

    }

});