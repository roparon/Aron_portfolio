# app.py

from __future__ import annotations

from flask import Flask, render_template

from config import site_config


PROJECTS = [
    {
        "number": "01",
        "title": "PinnaclePicks",
        "category": "Sports Analytics Platform",
        "summary": (
            "A Flask-based sports analytics platform built around structured "
            "match data, historical results, prediction presentation, "
            "subscription access, and an administrative workflow."
        ),
        "problem": (
            "Sports prediction interfaces often become difficult to maintain "
            "when upcoming fixtures, completed results, premium access, "
            "historical data, and administrative workflows are mixed together."
        ),
        "approach": (
            "The application uses Flask with an application factory, "
            "Flask-SQLAlchemy models, Jinja templates, route-level access "
            "control, reusable match helpers, and mobile-first interfaces. "
            "The data model separates matches, combination tickets, "
            "subscriptions, notifications, and media proof."
        ),
        "challenge": (
            "The difficult part was maintaining a trustworthy distinction "
            "between upcoming and concluded matches. Results are only archived "
            "when the match has a valid final score, preventing the application "
            "from inventing historical outcomes."
        ),
        "results": [
            "8 MB upload ceiling for proof media",
            "30-match default upcoming-match retrieval",
            "30-day default historical-results window",
            "Separate upcoming, finished and void match states",
        ],
        "stack": [
            "Python",
            "Flask",
            "Flask-SQLAlchemy",
            "Jinja2",
            "SQLite",
            "REST-style routes",
            "Responsive CSS",
        ],
        # Kept as configurable links rather than inventing unpublished URLs.
        "live_url": "",
        "repo_url": "",
        "live_label": "Live Demo",
        "repo_label": "GitHub Repo",
    },
    {
        "number": "02",
        "title": "Bomet Machineries",
        "category": "Agricultural Commerce",
        "summary": (
            "A mobile-first agricultural commerce experience designed around "
            "product discovery, shopping workflows, order management and "
            "search-friendly public pages."
        ),
        "problem": (
            "Agricultural equipment buyers need a straightforward way to "
            "discover products and move from product information to an order "
            "without navigating a desktop-first interface."
        ),
        "approach": (
            "The project uses Flask/Jinja on the backend and a deliberately "
            "lightweight frontend system. The interface is built mobile-first "
            "with semantic sections, responsive grids, high-contrast controls, "
            "large touch targets and a consistent green visual system."
        ),
        "challenge": (
            "The key frontend challenge was preventing the catalogue and "
            "transactional interface from becoming cramped on narrow devices. "
            "The layout was designed from a 320px baseline before progressively "
            "expanding into larger desktop layouts."
        ),
        "results": [
            "320px minimum mobile layout target",
            "44–48px minimum interactive controls",
            "1,380px maximum content container",
            "Production deployment on Vercel",
        ],
        "stack": [
            "Python",
            "Flask",
            "Jinja2",
            "HTML5",
            "CSS3",
            "JavaScript",
            "Vercel",
        ],
        "live_url": "https://bomet-machineries.vercel.app/",
        "repo_url": "https://github.com/roparon/AgroMart",
        "live_label": "Live Demo",
        "repo_label": "GitHub Repo",
    },
    {
        "number": "03",
        "title": "KuraSmart",
        "category": "Administrative Platform",
        "summary": (
            "A Flask application focused on structured administrative "
            "workflows, role-aware access, dashboard data and operational "
            "management."
        ),
        "problem": (
            "Operational platforms become fragile when authentication, "
            "permissions, dashboard data and administrative workflows are "
            "implemented independently without a consistent authorization model."
        ),
        "approach": (
            "The system uses Flask route organization, role-aware authorization, "
            "server-rendered interfaces and explicit backend validation. "
            "Administrative permissions are checked centrally rather than "
            "relying solely on frontend visibility."
        ),
        "challenge": (
            "A major debugging challenge involved dashboard data loading and "
            "authorization behavior. The solution was to trace the request "
            "through authentication, authorization, route handling and data "
            "serialization instead of treating the frontend error in isolation."
        ),
        "results": [
            "Role-aware administrative access",
            "Server-side authorization checks",
            "Modular Flask route structure",
            "Production-oriented debugging workflow",
        ],
        "stack": [
            "Python",
            "Flask",
            "Jinja2",
            "SQL",
            "HTML5",
            "CSS3",
            "JavaScript",
        ],
        "live_url": "",
        "repo_url": "",
        "live_label": "Live Demo",
        "repo_label": "GitHub Repo",
    },
    {
        "number": "04",
        "title": "County Portal",
        "category": "Public-Service Web Platform",
        "summary": (
            "A web platform concept focused on presenting structured county "
            "information through a responsive public-facing interface and "
            "maintainable Flask architecture."
        ),
        "problem": (
            "Public information systems have to balance dense information "
            "with simple navigation, accessibility and mobile usability."
        ),
        "approach": (
            "The architecture emphasizes server-rendered HTML, reusable "
            "templates, semantic sections, predictable URLs, responsive "
            "layouts and clear separation between presentation and backend "
            "logic."
        ),
        "challenge": (
            "The challenge was keeping information-heavy pages usable on "
            "small screens without simply hiding content. Responsive layout "
            "rules were used to change hierarchy and flow rather than remove "
            "important information."
        ),
        "results": [
            "Mobile-first responsive architecture",
            "Semantic HTML structure",
            "Reusable Flask/Jinja templates",
            "Touch-friendly public interface",
        ],
        "stack": [
            "Python",
            "Flask",
            "Jinja2",
            "HTML5",
            "CSS3",
            "JavaScript",
            "Git",
        ],
        "live_url": "",
        "repo_url": "",
        "live_label": "Live Demo",
        "repo_label": "GitHub Repo",
    },
]


SKILLS = {
    "Backend": [
        "Python",
        "Flask",
        "REST APIs",
        "SQL",
        "PostgreSQL",
        "Flask-SQLAlchemy",
        "Authentication",
        "Authorization",
    ],
    "Frontend": [
        "HTML5",
        "CSS3",
        "JavaScript ES6+",
        "Responsive Design",
        "Flexbox",
        "CSS Grid",
        "Accessibility",
        "SEO",
    ],
    "DevOps": [
        "Git",
        "GitHub",
        "Linux",
        "CI/CD",
        "Vercel",
        "Deployment",
        "Environment Configuration",
    ],
    "Tools": [
        "VS Code",
        "Postman",
        "Figma",
        "Chrome DevTools",
        "Git CLI",
        "Linux CLI",
    ],
}


def create_app() -> Flask:
    """Application factory."""

    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
    )

    app.config.update(
        SECRET_KEY="portfolio-development-key",
        SEND_FILE_MAX_AGE_DEFAULT=31536000,
    )

    @app.get("/")
    def index():
        return render_template(
            "index.html",
            config=site_config,
            projects=PROJECTS,
            skills=SKILLS,
        )

    @app.get("/health")
    def health():
        return {
            "status": "ok",
            "service": "aron-rop-portfolio",
        }

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )