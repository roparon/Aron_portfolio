/* static/js/main.js */

document.documentElement.classList.add("js-enabled");

document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.querySelector(".menu-toggle");
    const navigation = document.querySelector("#primary-navigation");

    if (menuToggle && navigation) {
        const navigationLinks = navigation.querySelectorAll("a");

        const closeMenu = () => {
            menuToggle.setAttribute("aria-expanded", "false");
            menuToggle.setAttribute(
                "aria-label",
                "Open navigation menu"
            );

            navigation.classList.remove("is-open");
        };

        menuToggle.addEventListener("click", () => {
            const isOpen =
                menuToggle.getAttribute("aria-expanded") === "true";

            menuToggle.setAttribute(
                "aria-expanded",
                String(!isOpen)
            );

            menuToggle.setAttribute(
                "aria-label",
                isOpen
                    ? "Open navigation menu"
                    : "Close navigation menu"
            );

            navigation.classList.toggle(
                "is-open",
                !isOpen
            );
        });

        navigationLinks.forEach((link) => {
            link.addEventListener("click", closeMenu);
        });

        window.addEventListener("resize", () => {
            if (window.innerWidth >= 768) {
                closeMenu();
            }
        });
    }

    const yearElement =
        document.querySelector("[data-current-year]");

    if (yearElement) {
        yearElement.textContent =
            String(new Date().getFullYear());
    }

    const revealElements =
        document.querySelectorAll(".reveal");

    if (
        "IntersectionObserver" in window &&
        revealElements.length > 0
    ) {
        const observer =
            new IntersectionObserver(
                (entries, currentObserver) => {
                    entries.forEach((entry) => {
                        if (!entry.isIntersecting) {
                            return;
                        }

                        entry.target.classList.add(
                            "is-visible"
                        );

                        currentObserver.unobserve(
                            entry.target
                        );
                    });
                },
                {
                    threshold: 0.12,
                    rootMargin: "0px 0px -40px 0px",
                }
            );

        revealElements.forEach((element) => {
            observer.observe(element);
        });
    } else {
        revealElements.forEach((element) => {
            element.classList.add("is-visible");
        });
    }
});