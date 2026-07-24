import sys
from pathlib import Path

# Ensure imports work when running from the AURA_OS folder directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from PySide6.QtWidgets import QApplication
from AURA_OS.database.app.core.logger import Logger
from AURA_OS.database.app.core.database import initialize_database
from AURA_OS.database.app.ui.task_view import TaskView
from AURA_OS.database.app.ui.main_window import MainWindow


def main():
    Logger.setup()
    initialize_database()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(
        app.exec()
    )
if __name__ == "__main__":

    main()