from AURA_OS.database.app.core.config import Config
from AURA_OS.database.app.services.file_service import FileService
from AURA_OS.database.app.services.note_service import NoteService


def test_notes_and_files_workflow():
    note = NoteService.create_note(
        title="Test Note",
        category="Work",
        content="This is a test note."
    )
    notes = NoteService.get_notes()
    assert any(n.id == note.id for n in notes)

    folder = FileService.create_folder("feature-test")
    assert folder.exists()

    Config.save_preferences(username="AURA User", theme="dark")
    assert Config.USERNAME == "AURA User"
    assert Config.THEME == "dark"
