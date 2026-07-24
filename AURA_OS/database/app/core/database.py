"""
Database Engine
"""

from sqlalchemy import create_engine

from AURA_OS.database.app.core.config import Config

from AURA_OS.database.app.database.models import Base

import AURA_OS.database.app.models


DATABASE_URL = f"sqlite:///{Config.DATABASE_FILE}"


engine = create_engine(
    DATABASE_URL,
    echo=False,
)


def initialize_database():

    Config.create_directories()

    Base.metadata.create_all(bind=engine)