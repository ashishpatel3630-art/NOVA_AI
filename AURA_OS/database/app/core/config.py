"""Application configuration settings."""

import json
import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    APP_NAME: str = os.getenv("APP_NAME", "AURA")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    DATABASE_DIR = BASE_DIR / "database"
    DATABASE_FILE = DATABASE_DIR / os.getenv("DATABASE_NAME", "aura.db")
    LOG_DIR = BASE_DIR / "logs"
    LOG_FILE = LOG_DIR / "aura.log"
    SETTINGS_FILE = BASE_DIR / "database" / "settings.json"

    USERNAME: str = os.getenv("USERNAME", "User")
    THEME: str = os.getenv("THEME", "dark")

    @classmethod
    def create_directories(cls):
        cls.DATABASE_DIR.mkdir(exist_ok=True)
        cls.LOG_DIR.mkdir(exist_ok=True)

    @classmethod
    def load_preferences(cls):
        cls.create_directories()
        if not cls.SETTINGS_FILE.exists():
            return {"username": cls.USERNAME, "theme": cls.THEME}
        with cls.SETTINGS_FILE.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
            cls.USERNAME = data.get("username", cls.USERNAME)
            cls.THEME = data.get("theme", cls.THEME)
            return {"username": cls.USERNAME, "theme": cls.THEME}

    @classmethod
    def save_preferences(cls, username: str | None = None, theme: str | None = None):
        cls.create_directories()
        if username is not None:
            cls.USERNAME = username
        if theme is not None:
            cls.THEME = theme
        payload = {"username": cls.USERNAME, "theme": cls.THEME}
        with cls.SETTINGS_FILE.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
        return payload