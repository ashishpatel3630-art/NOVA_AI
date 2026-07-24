"""Session helpers for database access."""

from sqlalchemy.orm import Session, sessionmaker

from AURA_OS.database.app.core.database import engine


SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def get_session() -> Session:
    """Create a new database session."""
    return SessionLocal()
