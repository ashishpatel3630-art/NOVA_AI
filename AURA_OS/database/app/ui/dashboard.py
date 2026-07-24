"""
AURA Dashboard Interface
"""


from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel

from AURA_OS.database.app.services.note_service import NoteService
from AURA_OS.database.app.services.task_service import TaskService
from AURA_OS.database.app.ui.components.card import Card
from AURA_OS.database.app.ui.components.table import AuraTable



class Dashboard(QWidget):


    def __init__(self):

        super().__init__()


        self.setup_ui()



    def setup_ui(self):


        main_layout = QVBoxLayout()


        title = QLabel(
            "AURA Dashboard"
        )


        main_layout.addWidget(
            title
        )


        cards_layout = QHBoxLayout()

        cards = [
            Card("Total Tasks", str(TaskService.get_total_tasks())),
            Card("Completed", str(TaskService.get_completed_tasks())),
            Card("Pending", str(TaskService.get_pending_tasks())),
            Card("Notes", str(NoteService.get_total_notes())),
        ]

        for card in cards:
            cards_layout.addWidget(card)

        main_layout.addLayout(cards_layout)



        activity_title = QLabel(
            "Recent Activities"
        )


        main_layout.addWidget(
            activity_title
        )


        self.activity_table = AuraTable(["Action", "Date"])
        self.activity_table.add_row(["Tasks loaded", "Today"])
        self.activity_table.add_row(["Notes available", "Today"])
        self.activity_table.add_row(["System ready", "Now"])

        main_layout.addWidget(self.activity_table)


        self.setLayout(
            main_layout
        )