"""Table widget component for the dashboard and task views."""

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem


class AuraTable(QTableWidget):
    def __init__(self, columns: list[str]):
        super().__init__()
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)

    def add_row(self, data: list[str]):
        row = self.rowCount()
        self.insertRow(row)
        for index, value in enumerate(data):
            self.setItem(row, index, QTableWidgetItem(str(value)))
