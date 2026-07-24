"""
AURA Sidebar Navigation
"""

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
)

from PySide6.QtCore import Signal



class Sidebar(QWidget):

    page_changed = Signal(str)


    def __init__(self):

        super().__init__()

        self.setup_ui()


    def setup_ui(self):

        layout = QVBoxLayout()


        buttons = [
            ("Dashboard", "dashboard"),
            ("Tasks", "tasks"),
            ("Notes", "notes"),
            ("Files", "files"),
            ("Analytics", "analytics"),
            ("Utilities", "utilities"),
            ("Settings", "settings"),
        ]


        for text, page in buttons:

            button = QPushButton(text)

            button.clicked.connect(
                lambda checked=False,
                p=page:
                self.change_page(p)
            )


            layout.addWidget(button)


        layout.addStretch()


        self.setLayout(layout)


    def change_page(self, page):

        self.page_changed.emit(page)