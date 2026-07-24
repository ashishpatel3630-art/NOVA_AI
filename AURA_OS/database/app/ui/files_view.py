"""File manager view for AURA."""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox

from AURA_OS.database.app.services.file_service import FileService


class FilesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.load_files()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("File Organizer"))

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search files")
        layout.addWidget(self.search_input)

        buttons = QHBoxLayout()
        create_button = QPushButton("Create Folder")
        create_button.clicked.connect(self.create_folder)
        buttons.addWidget(create_button)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_files)
        buttons.addWidget(search_button)
        layout.addLayout(buttons)

        self.files_list = QListWidget()
        layout.addWidget(self.files_list)
        self.setLayout(layout)

    def load_files(self):
        self.files_list.clear()
        for path in FileService.search_files(""):
            self.files_list.addItem(QListWidgetItem(str(path)))

    def create_folder(self):
        name = self.search_input.text().strip() or "new_folder"
        folder = FileService.create_folder(name)
        self.files_list.addItem(str(folder))

    def search_files(self):
        keyword = self.search_input.text().strip()
        self.files_list.clear()
        for path in FileService.search_files(keyword):
            self.files_list.addItem(QListWidgetItem(str(path)))
