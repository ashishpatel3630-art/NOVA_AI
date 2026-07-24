"""Dialog components for the AURA UI."""

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QTextEdit, QComboBox, QPushButton


class TaskDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Task")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.title = QLineEdit()
        self.title.setPlaceholderText("Task Title")

        self.description = QTextEdit()
        self.description.setPlaceholderText("Description")

        self.priority = QComboBox()
        self.priority.addItems(["Low", "Medium", "High"])

        self.deadline = QLineEdit()
        self.deadline.setPlaceholderText("Deadline")

        self.save_button = QPushButton("Save Task")
        self.save_button.clicked.connect(self.accept)

        layout.addWidget(self.title)
        layout.addWidget(self.description)
        layout.addWidget(self.priority)
        layout.addWidget(self.deadline)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
