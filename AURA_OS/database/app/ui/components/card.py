"""Dashboard card component."""

from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class Card(QFrame):
    def __init__(self, title: str, value: str):
        super().__init__()
        layout = QVBoxLayout()
        self.title = QLabel(title)
        self.value = QLabel(value)
        layout.addWidget(self.title)
        layout.addWidget(self.value)
        self.setLayout(layout)
        self.setMinimumHeight(120)
