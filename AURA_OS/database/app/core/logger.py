"""
AURA Logging System
"""

import logging

from AURA_OS.database.app.core.config import Config



class Logger:

    @staticmethod
    def setup():
        Config.create_directories()
        logging.basicConfig(

            filename=Config.LOG_FILE,

            level=logging.INFO,

            format=
            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"

        )


        logging.info(
            "AURA Application Started"
        )