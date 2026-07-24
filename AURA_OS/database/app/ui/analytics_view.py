"""Analytics and productivity view for AURA."""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from AURA_OS.database.app.services.task_service import TaskService
from AURA_OS.database.app.services.note_service import NoteService


class AnalyticsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Productivity Analytics"))
        layout.addWidget(QLabel(f"Total Tasks: {TaskService.get_total_tasks()}"))
        layout.addWidget(QLabel(f"Completed Tasks: {TaskService.get_completed_tasks()}"))
        layout.addWidget(QLabel(f"Pending Tasks: {TaskService.get_pending_tasks()}"))
        layout.addWidget(QLabel(f"Total Notes: {NoteService.get_total_notes()}"))
        self.setLayout(layout)
