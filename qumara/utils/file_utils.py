"""File utility functions."""

from pathlib import Path
from typing import List, Optional

from qumara.utils.logger import Logger

logger = Logger.get_logger(__name__)


class FileUtils:
    """File operation utilities."""

    @staticmethod
    def ensure_dir(path: str) -> Path:
        """Ensure directory exists, create if needed.

        Args:
            path: Directory path

        Returns:
            Path object
        """
        directory = Path(path)
        directory.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Ensured directory exists: {directory}")
        return directory

    @staticmethod
    def ensure_file_dir(file_path: str) -> Path:
        """Ensure directory for file exists.

        Args:
            file_path: File path

        Returns:
            Parent directory path
        """
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path.parent

    @staticmethod
    def list_files(directory: str, pattern: str = "*") -> List[Path]:
        """List files in directory.

        Args:
            directory: Directory path
            pattern: File pattern (glob)

        Returns:
            List of file paths
        """
        dir_path = Path(directory)
        if not dir_path.exists():
            logger.warning(f"Directory not found: {directory}")
            return []
        return list(dir_path.glob(pattern))

    @staticmethod
    def read_file(file_path: str) -> str:
        """Read file contents.

        Args:
            file_path: Path to file

        Returns:
            File contents
        """
        path = Path(file_path)
        return path.read_text()

    @staticmethod
    def write_file(file_path: str, content: str, append: bool = False) -> None:
        """Write to file.

        Args:
            file_path: Path to file
            content: Content to write
            append: Append if True, overwrite if False
        """
        path = Path(file_path)
        FileUtils.ensure_file_dir(file_path)
        if append:
            path.write_text(path.read_text() + content)
        else:
            path.write_text(content)
        logger.debug(f"Wrote to file: {file_path}")
