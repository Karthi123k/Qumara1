"""Logging utility for QuMARA.

Provides centralized logging with console and file output.
"""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


class Logger:
    """Centralized logging utility."""

    _loggers: dict = {}
    _log_dir: Optional[Path] = None
    _log_level: str = "INFO"

    @classmethod
    def configure(
        cls,
        log_level: str = "INFO",
        log_dir: Optional[str] = None,
    ) -> None:
        """Configure logging globally.

        Args:
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_dir: Directory for log files. If None, logs only to console.
        """
        cls._log_level = log_level
        if log_dir:
            cls._log_dir = Path(log_dir)
            cls._log_dir.mkdir(parents=True, exist_ok=True)

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """Get or create a logger.

        Args:
            name: Logger name (typically __name__)

        Returns:
            Configured logger instance
        """
        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, cls._log_level))

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, cls._log_level))
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # File handler
        if cls._log_dir:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = cls._log_dir / f"{name}_{timestamp}.log"
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(getattr(logging, cls._log_level))
            file_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        cls._loggers[name] = logger
        return logger
