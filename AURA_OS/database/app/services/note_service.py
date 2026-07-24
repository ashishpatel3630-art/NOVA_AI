"""Note business logic."""

from AURA_OS.database.app.database.session import get_session
from AURA_OS.database.app.models.note import Note


class NoteService:
    @staticmethod
    def get_total_notes() -> int:
        session = get_session()
        try:
            return session.query(Note).count()
        finally:
            session.close()

    @staticmethod
    def get_notes():
        session = get_session()
        try:
            return session.query(Note).order_by(Note.created_at.desc()).all()
        finally:
            session.close()

    @staticmethod
    def create_note(title: str, category: str, content: str):
        session = get_session()
        try:
            note = Note(title=title, category=category, content=content)
            session.add(note)
            session.commit()
            return note
        finally:
            session.close()

    @staticmethod
    def update_note(note_id: int, title: str, category: str, content: str):
        session = get_session()
        try:
            note = session.get(Note, note_id)
            if note is None:
                return None
            note.title = title
            note.category = category
            note.content = content
            session.commit()
            return note
        finally:
            session.close()

    @staticmethod
    def delete_note(note_id: int):
        session = get_session()
        try:
            note = session.get(Note, note_id)
            if note is not None:
                session.delete(note)
                session.commit()
            return note
        finally:
            session.close()

    @staticmethod
    def search_notes(keyword: str):
        session = get_session()
        try:
            pattern = f"%{keyword}%"
            return session.query(Note).filter(
                Note.title.like(pattern) | Note.content.like(pattern) | Note.category.like(pattern)
            ).order_by(Note.created_at.desc()).all()
        finally:
            session.close()