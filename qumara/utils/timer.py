"""Timer utility for measuring operation duration."""

import time
from contextlib import contextmanager
from typing import Generator, Optional


class Timer:
    """Simple timer for measuring duration."""

    def __init__(self, name: str = "Operation"):
        """Initialize timer.

        Args:
            name: Name of the operation being timed
        """
        self.name = name
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None

    def start(self) -> None:
        """Start the timer."""
        self.start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the timer and return elapsed time in milliseconds.

        Returns:
            Elapsed time in milliseconds
        """
        self.end_time = time.perf_counter()
        if self.start_time is None:
            return 0.0
        return (self.end_time - self.start_time) * 1000

    def elapsed_ms(self) -> float:
        """Get elapsed time in milliseconds.

        Returns:
            Elapsed time in milliseconds
        """
        if self.start_time is None:
            return 0.0
        current_time = time.perf_counter()
        return (current_time - self.start_time) * 1000

    def __enter__(self):
        """Context manager entry."""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop()


@contextmanager
def measure_time(name: str = "Operation") -> Generator[Timer, None, None]:
    """Context manager for measuring operation time.

    Args:
        name: Name of the operation

    Yields:
        Timer object
    """
    timer = Timer(name)
    timer.start()
    try:
        yield timer
    finally:
        elapsed = timer.stop()
