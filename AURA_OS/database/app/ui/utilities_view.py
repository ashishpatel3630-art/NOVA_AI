"""Utility tools view for AURA."""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

from AURA_OS.database.app.utilities.calculator import Calculator
from AURA_OS.database.app.utilities.system_info import SystemInfo
from AURA_OS.database.app.utilities.timer import Timer


class UtilitiesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Utilities"))

        calc_button = QPushButton("Test Calculator")
        calc_button.clicked.connect(self.show_calc_result)
        layout.addWidget(calc_button)

        info_button = QPushButton("Show System Info")
        info_button.clicked.connect(self.show_system_info)
        layout.addWidget(info_button)

        timer_button = QPushButton("Start Simple Timer")
        timer_button.clicked.connect(self.show_timer)
        layout.addWidget(timer_button)

        self.setLayout(layout)

    def show_calc_result(self):
        result = Calculator.add(2, 3)
        QMessageBox.information(self, "Calculator", f"2 + 3 = {result}")

    def show_system_info(self):
        info = SystemInfo.get_info()
        QMessageBox.information(self, "System Info", str(info))

    def show_timer(self):
        timer = Timer(seconds=10)
        timer.start()
        QMessageBox.information(self, "Timer", f"Timer started. Remaining: {timer.remaining()}")
