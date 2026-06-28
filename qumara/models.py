"""Data models and dataclasses for QuMARA."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class TokenType(str, Enum):
    """JWT token types."""

    ACCESS = "access"
    REFRESH = "refresh"


@dataclass
class AuthenticationMetrics:
    """Authentication operation metrics."""

    algorithm: str
    signing_time_ms: float
    verification_time_ms: float
    jwt_size_bytes: int
    signature_size_bytes: int
    cpu_usage_percent: float
    memory_usage_mb: float
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class TelemetryRecord:
    """Runtime telemetry record."""

    timestamp: datetime
    algorithm: str
    auth_latency_ms: float
    verify_latency_ms: float
    jwt_size_bytes: int
    signature_size_bytes: int
    cpu_percent: float
    memory_mb: float
    network_overhead_bytes: int
    success_rate: float
    throughput_rps: float

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
            "network_overhead_bytes": self.network_overhead_bytes,
            "success_rate": self.success_rate,
            "throughput_rps": self.throughput_rps,
        }


@dataclass
class BenchmarkRecord:
    """Benchmark execution record."""

    timestamp: datetime
    algorithm: str
    security_level: str
    concurrent_users: int
    auth_latency_ms: float
    verify_latency_ms: float
    jwt_size_bytes: int
    signature_size_bytes: int
    throughput_rps: float
    cpu_percent: float
    memory_mb: float
    network_bandwidth_kbps: float
    success_rate: float
    error_rate: float

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "timestamp": self.timestamp.isoformat(),
            "algorithm": self.algorithm,
            "security_level": self.security_level,
            "concurrent_users": self.concurrent_users,
            "auth_latency_ms": self.auth_latency_ms,
            "verify_latency_ms": self.verify_latency_ms,
            "jwt_size_bytes": self.jwt_size_bytes,
            "signature_size_bytes": self.signature_size_bytes,
            "throughput_rps": self.throughput_rps,
            "cpu_percent": self.cpu_percent,
            "memory_mb": self.memory_mb,
            "network_bandwidth_kbps": self.network_bandwidth_kbps,
            "success_rate": self.success_rate,
            "error_rate": self.error_rate,
        }


@dataclass
class TrainingMetrics:
    """RL training metrics."""

    episode: int
    total_reward: float
    average_latency_ms: float
    algorithm_selected: str
    success_rate: float


@dataclass
class EvaluationMetrics:
    """RL evaluation metrics."""

    total_episodes: int
    average_reward: float
    average_latency_ms: float
    algorithm_distribution: Dict[str, float]
    success_rate: float
    security_level: str


# Pydantic models for API


class LoginRequest(BaseModel):
    """Login request."""

    username: str
    password: str
    intent_profile: Optional[str] = "balanced"


class TokenResponse(BaseModel):
    """Token response."""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
    algorithm: str


class RefreshTokenRequest(BaseModel):
    """Refresh token request."""

    refresh_token: str


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    service: str
    version: str
    timestamp: datetime = Field(default_factory=datetime.now)


class MetricsResponse(BaseModel):
    """Metrics response."""

    metrics: Dict[str, float]
    timestamp: datetime = Field(default_factory=datetime.now)


class UserProfile(BaseModel):
    """User profile."""

    user_id: str
    username: str
    email: str
    created_at: datetime
    last_login: Optional[datetime] = None


class ErrorResponse(BaseModel):
    """Error response."""

    error: str
    message: str
    timestamp: datetime = Field(default_factory=datetime.now)
