"""Settings view for AURA."""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox

from AURA_OS.database.app.core.config import Config


class SettingsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Application Settings"))

        self.username_input = QLineEdit(Config.USERNAME)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(QLabel("Username"))
        layout.addWidget(self.username_input)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["dark", "light"])
        self.theme_combo.setCurrentText(Config.THEME)
        layout.addWidget(QLabel("Theme"))
        layout.addWidget(self.theme_combo)

        save_button = QPushButton("Save Settings")
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_settings(self):
        Config.save_preferences(
            username=self.username_input.text() or Config.USERNAME,
            theme=self.theme_combo.currentText(),
        )
        QMessageBox.information(self, "Saved", "Settings saved successfully")
