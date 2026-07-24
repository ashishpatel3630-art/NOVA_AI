"""System information helpers."""

import os
import platform
import shutil
import socket


class SystemInfo:
    @staticmethod
    def get_info() -> dict:
        return {
            "platform": platform.platform(),
            "system": platform.system(),
            "release": platform.release(),
            "python_version": platform.python_version(),
            "hostname": socket.gethostname(),
            "cpu_count": os.cpu_count(),
            "disk_free": shutil.disk_usage("/").free,
        }
