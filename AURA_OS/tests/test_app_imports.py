import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from AURA_OS.database.app.core.database import initialize_database
from AURA_OS.database.app.services.note_service import NoteService
from AURA_OS.database.app.services.task_service import TaskService
from AURA_OS.database.app.ui.dashboard import Dashboard
from AURA_OS.database.app.ui.main_window import MainWindow
from AURA_OS.database.app.utilities.timer import Timer


def test_app_modules_import_and_initialize():
    app = QApplication.instance() or QApplication([])
    initialize_database()

    assert isinstance(NoteService.get_total_notes(), int)
    assert isinstance(TaskService.get_total_tasks(), int)

    dashboard = Dashboard()
    window = MainWindow()
    timer = Timer()

    assert dashboard is not None
    assert window is not None
    assert timer is not None

    app.processEvents()
