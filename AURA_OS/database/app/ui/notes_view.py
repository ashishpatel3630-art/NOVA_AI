"""Notes management view for AURA."""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox

from AURA_OS.database.app.services.note_service import NoteService


class NotesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.load_notes()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Notes"))

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Title")
        layout.addWidget(self.title_input)

        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("Category")
        layout.addWidget(self.category_input)

        self.content_input = QTextEdit()
        self.content_input.setPlaceholderText("Write your note here")
        layout.addWidget(self.content_input)

        buttons = QHBoxLayout()
        save_button = QPushButton("Save Note")
        save_button.clicked.connect(self.save_note)
        buttons.addWidget(save_button)

        delete_button = QPushButton("Delete Note")
        delete_button.clicked.connect(self.delete_note)
        buttons.addWidget(delete_button)
        layout.addLayout(buttons)

        self.notes_list = QListWidget()
        self.notes_list.itemClicked.connect(self.select_note)
        layout.addWidget(self.notes_list)
        self.setLayout(layout)

    def load_notes(self):
        self.notes_list.clear()
        for note in NoteService.get_notes():
            self.notes_list.addItem(QListWidgetItem(f"{note.title} [{note.category}]"))

    def save_note(self):
        title = self.title_input.text().strip()
        category = self.category_input.text().strip() or "General"
        content = self.content_input.toPlainText().strip()
        if not title:
            QMessageBox.warning(self, "Missing title", "Please enter a title")
            return
        NoteService.create_note(title, category, content)
        self.load_notes()
        self.title_input.clear(); self.category_input.clear(); self.content_input.clear()

    def select_note(self, item):
        self.title_input.setText(item.text().split(" [")[0])

    def delete_note(self):
        current_row = self.notes_list.currentRow()
        if current_row < 0:
            return
        note_title = self.notes_list.item(current_row).text()
        QMessageBox.information(self, "Note", f"Selected note: {note_title}")
