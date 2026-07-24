"""Task management view for AURA."""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

from AURA_OS.database.app.services.task_service import TaskService
from AURA_OS.database.app.ui.components.dialogs import TaskDialog
from AURA_OS.database.app.ui.components.table import AuraTable


class TaskView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.load_tasks()

    def setup_ui(self):
        layout = QVBoxLayout()
        top = QHBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Tasks...")
        self.search.textChanged.connect(self.search_tasks)

        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)

        delete_button = QPushButton("Delete Task")
        delete_button.clicked.connect(self.delete_task)

        top.addWidget(self.search)
        top.addWidget(add_button)
        top.addWidget(delete_button)

        layout.addLayout(top)

        self.table = AuraTable(["ID", "Title", "Priority", "Status", "Deadline"])
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_tasks(self):
        self.table.setRowCount(0)
        tasks = TaskService.get_tasks()
        for task in tasks:
            self.table.add_row([task.id, task.title, task.priority, task.status, task.deadline])

    def add_task(self):
        dialog = TaskDialog()
        if dialog.exec():
            TaskService.create_task(
                dialog.title.text(),
                dialog.description.toPlainText(),
                dialog.priority.currentText(),
                dialog.deadline.text(),
            )
            self.load_tasks()

    def delete_task(self):
        row = self.table.currentRow()
        if row >= 0:
            task_id = self.table.item(row, 0).text()
            TaskService.delete_task(int(task_id))
            self.load_tasks()

    def search_tasks(self):
        keyword = self.search.text()
        self.table.setRowCount(0)
        tasks = TaskService.search_task(keyword)
        for task in tasks:
            self.table.add_row([task.id, task.title, task.priority, task.status, task.deadline])
