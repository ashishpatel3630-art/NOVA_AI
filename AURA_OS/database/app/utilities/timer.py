"""Simple timer utility for AURA."""

from __future__ import annotations

import time
from typing import Optional


class Timer:
    """Minimal countdown/timer helper."""

    def __init__(self, seconds: Optional[int] = None):
        self.seconds = seconds
        self._start_time: Optional[float] = None

    def start(self) -> None:
        self._start_time = time.time()

    def elapsed(self) -> float:
        if self._start_time is None:
            return 0.0
        return time.time() - self._start_time

    def remaining(self) -> Optional[float]:
        if self.seconds is None:
            return None
        return max(0.0, self.seconds - self.elapsed())
