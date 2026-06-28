"""Network utility functions."""

import socket
from typing import Tuple

from qumara.utils.logger import Logger

logger = Logger.get_logger(__name__)


class NetworkUtils:
    """Network utilities."""

    @staticmethod
    def is_port_available(host: str, port: int) -> bool:
        """Check if port is available.

        Args:
            host: Host address
            port: Port number

        Returns:
            True if port is available
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind((host, port))
                return True
        except OSError:
            return False

    @staticmethod
    def find_available_port(host: str = "127.0.0.1", start_port: int = 8000) -> int:
        """Find an available port.

        Args:
            host: Host address
            start_port: Starting port number

        Returns:
            Available port number
        """
        port = start_port
        while port < 65535:
            if NetworkUtils.is_port_available(host, port):
                logger.info(f"Found available port: {port}")
                return port
            port += 1
        raise RuntimeError(f"No available ports found starting from {start_port}")

    @staticmethod
    def get_local_ip() -> str:
        """Get local IP address.

        Returns:
            Local IP address
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.connect(("8.8.8.8", 80))
                return sock.getsockname()[0]
        except Exception as e:
            logger.error(f"Failed to get local IP: {e}")
            return "127.0.0.1"
