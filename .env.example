# config.py

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class SiteConfig:
    """Runtime configuration for the portfolio."""

    name: str = os.getenv("SITE_NAME", "Aron Rop")
    role: str = os.getenv("SITE_ROLE", "Full-Stack Software Engineer")
    email: str = os.getenv("CONTACT_EMAIL", "aaronrop40@gmail.com")

    github_url: str = os.getenv(
        "GITHUB_URL",
        "https://github.com/roparon",
    )

    linkedin_url: str = os.getenv("LINKEDIN_URL", "")

    whatsapp_url: str = os.getenv("WHATSAPP_URL", "")

    site_url: str = os.getenv(
        "SITE_URL",
        "https://your-domain.example",
    )

    resume_path: str = os.getenv(
        "RESUME_PATH",
        "/static/resume/Aron-Rop-Resume.pdf",
    )

    contact_subject: str = os.getenv(
        "CONTACT_SUBJECT",
        "Software Engineering Opportunity — Aron Rop",
    )


site_config = SiteConfig()