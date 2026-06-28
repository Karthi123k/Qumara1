"""Metrics utilities for QuMARA."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass
class MetricsRecord:
    """Record of performance metrics."""

    timestamp: datetime = field(default_factory=datetime.now)
    algorithm: str = ""
    auth_latency_ms: float = 0.0
    verify_latency_ms: float = 0.0
    jwt_size_bytes: int = 0
    signature_size_bytes: int = 0
    cpu_percent: float = 0.0
    memory_mb: float = 0.0
    bandwidth_kbps: float = 0.0
    success_rate: float = 0.0
    throughput_rps: float = 0.0

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "timestamp": self.timestamp.isoformat(),
            "algorithm": self.algorithm,
            "auth_latency_ms": self.auth_latency_ms,
            "verify_latency_ms": self.verify_latency_ms,
            "jwt_size_bytes": self.jwt_size_bytes,
            "signature_size_bytes": self.signature_size_bytes,
            "cpu_percent": self.cpu_percent,
            "memory_mb": self.memory_mb,
            "bandwidth_kbps": self.bandwidth_kbps,
            "success_rate": self.success_rate,
            "throughput_rps": self.throughput_rps,
        }


class MetricsAggregator:
    """Aggregate metrics over time."""

    def __init__(self):
        """Initialize aggregator."""
        self.records: List[MetricsRecord] = []

    def add(self, record: MetricsRecord) -> None:
        """Add a metrics record."""
        self.records.append(record)

    def get_average(self) -> Dict:
        """Get average metrics."""
        if not self.records:
            return {}

        avg = {
            "auth_latency_ms": sum(r.auth_latency_ms for r in self.records) / len(self.records),
            "verify_latency_ms": sum(r.verify_latency_ms for r in self.records)
            / len(self.records),
            "jwt_size_bytes": sum(r.jwt_size_bytes for r in self.records) / len(self.records),
            "signature_size_bytes": sum(r.signature_size_bytes for r in self.records)
            / len(self.records),
            "cpu_percent": sum(r.cpu_percent for r in self.records) / len(self.records),
            "memory_mb": sum(r.memory_mb for r in self.records) / len(self.records),
            "bandwidth_kbps": sum(r.bandwidth_kbps for r in self.records) / len(self.records),
            "success_rate": sum(r.success_rate for r in self.records) / len(self.records),
            "throughput_rps": sum(r.throughput_rps for r in self.records) / len(self.records),
        }
        return avg

    def get_min(self) -> Dict:
        """Get minimum metrics."""
        if not self.records:
            return {}

        return {
            "auth_latency_ms": min(r.auth_latency_ms for r in self.records),
            "verify_latency_ms": min(r.verify_latency_ms for r in self.records),
            "cpu_percent": min(r.cpu_percent for r in self.records),
        }

    def get_max(self) -> Dict:
        """Get maximum metrics."""
        if not self.records:
            return {}

        return {
            "auth_latency_ms": max(r.auth_latency_ms for r in self.records),
            "verify_latency_ms": max(r.verify_latency_ms for r in self.records),
            "cpu_percent": max(r.cpu_percent for r in self.records),
        }
