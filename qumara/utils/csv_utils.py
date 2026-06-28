"""CSV utility functions."""

import csv
from pathlib import Path
from typing import Any, Dict, List

from qumara.utils.logger import Logger

logger = Logger.get_logger(__name__)


class CSVUtils:
    """CSV file operations."""

    @staticmethod
    def write_records(file_path: str, records: List[Dict[str, Any]], append: bool = False) -> None:
        """Write records to CSV file.

        Args:
            file_path: Path to CSV file
            records: List of record dictionaries
            append: Append if True, overwrite if False
        """
        if not records:
            logger.warning("No records to write")
            return

        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        fieldnames = list(records[0].keys())
        mode = "a" if append and path.exists() else "w"
        write_header = mode == "w"

        with open(path, mode, newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if write_header:
                writer.writeheader()
            writer.writerows(records)

        logger.info(f"Wrote {len(records)} records to {file_path}")

    @staticmethod
    def read_records(file_path: str) -> List[Dict[str, Any]]:
        """Read records from CSV file.

        Args:
            file_path: Path to CSV file

        Returns:
            List of record dictionaries
        """
        path = Path(file_path)
        if not path.exists():
            logger.warning(f"CSV file not found: {file_path}")
            return []

        records = []
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            records = list(reader)

        logger.info(f"Read {len(records)} records from {file_path}")
        return records

    @staticmethod
    def append_record(file_path: str, record: Dict[str, Any]) -> None:
        """Append a single record to CSV file.

        Args:
            file_path: Path to CSV file
            record: Record dictionary
        """
        CSVUtils.write_records(file_path, [record], append=True)
