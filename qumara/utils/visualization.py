"""Visualization utilities for QuMARA."""

from pathlib import Path
from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np

from qumara.utils.logger import Logger

logger = Logger.get_logger(__name__)


class Visualization:
    """Visualization utilities."""

    @staticmethod
    def plot_latency_comparison(
        algorithms: List[str],
        auth_latencies: List[float],
        verify_latencies: List[float],
        output_path: str = "latency_comparison.png",
    ) -> None:
        """Plot latency comparison.

        Args:
            algorithms: List of algorithm names
            auth_latencies: Authentication latencies
            verify_latencies: Verification latencies
            output_path: Output file path
        """
        x = np.arange(len(algorithms))
        width = 0.35

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(x - width / 2, auth_latencies, width, label="Auth Latency")
        ax.bar(x + width / 2, verify_latencies, width, label="Verify Latency")

        ax.set_xlabel("Algorithm")
        ax.set_ylabel("Latency (ms)")
        ax.set_title("Authentication Latency Comparison")
        ax.set_xticks(x)
        ax.set_xticklabels(algorithms, rotation=45)
        ax.legend()
        ax.grid(axis="y", alpha=0.3)

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()
        logger.info(f"Saved latency comparison plot to {output_path}")

    @staticmethod
    def plot_resource_usage(
        algorithms: List[str],
        cpu_usage: List[float],
        memory_usage: List[float],
        output_path: str = "resource_usage.png",
    ) -> None:
        """Plot resource usage comparison.

        Args:
            algorithms: List of algorithm names
            cpu_usage: CPU usage percentages
            memory_usage: Memory usage in MB
            output_path: Output file path
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        ax1.bar(algorithms, cpu_usage, color="orange")
        ax1.set_ylabel("CPU Usage (%)")
        ax1.set_title("CPU Usage Comparison")
        ax1.set_xticklabels(algorithms, rotation=45)
        ax1.grid(axis="y", alpha=0.3)

        ax2.bar(algorithms, memory_usage, color="green")
        ax2.set_ylabel("Memory Usage (MB)")
        ax2.set_title("Memory Usage Comparison")
        ax2.set_xticklabels(algorithms, rotation=45)
        ax2.grid(axis="y", alpha=0.3)

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.close()
        logger.info(f"Saved resource usage plot to {output_path}")
