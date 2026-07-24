"""AURA main window."""

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel

from AURA_OS.database.app.ui.analytics_view import AnalyticsView
from AURA_OS.database.app.ui.dashboard import Dashboard
from AURA_OS.database.app.ui.files_view import FilesView
from AURA_OS.database.app.ui.notes_view import NotesView
from AURA_OS.database.app.ui.settings_view import SettingsView
from AURA_OS.database.app.ui.sidebar import Sidebar
from AURA_OS.database.app.ui.task_view import TaskView
from AURA_OS.database.app.ui.utilities_view import UtilitiesView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AURA - Personal Digital OS")
        self.resize(1200, 700)
        self.setup_ui()

    def setup_ui(self):
        container = QWidget()
        self.layout = QHBoxLayout()
        self.sidebar = Sidebar()
        self.content = Dashboard()

        self.sidebar.page_changed.connect(self.change_page)

        self.layout.addWidget(self.sidebar)
        self.layout.addWidget(self.content)

        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def change_page(self, page: str):
        if self.content is not None:
            self.layout.removeWidget(self.content)
            self.content.deleteLater()

        if page == "tasks":
            self.content = TaskView()
        elif page == "dashboard":
            self.content = Dashboard()
        elif page == "notes":
            self.content = NotesView()
        elif page == "files":
            self.content = FilesView()
        elif page == "analytics":
            self.content = AnalyticsView()
        elif page == "utilities":
            self.content = UtilitiesView()
        elif page == "settings":
            self.content = SettingsView()
        else:
            self.content = QLabel(f"{page.title()} Page Coming Soon")

        self.layout.addWidget(self.content)