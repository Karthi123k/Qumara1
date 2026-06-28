"""Global constants for QuMARA.

Defines authentication algorithms, intent profiles, metric names,
and other system-wide constants.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict


class AuthenticationAlgorithm(str, Enum):
    """Post-quantum authentication algorithms."""

    ML_DSA_44 = "ML-DSA-44"
    ML_DSA_65 = "ML-DSA-65"
    ML_DSA_87 = "ML-DSA-87"
    SLH_DSA_128 = "SLH-DSA-128"
    SLH_DSA_192 = "SLH-DSA-192"
    SLH_DSA_256 = "SLH-DSA-256"


class IntentProfile(str, Enum):
    """Runtime intent profiles for authentication policy optimization."""

    SECURITY_FIRST = "security_first"
    PERFORMANCE_FIRST = "performance_first"
    BALANCED = "balanced"
    RESOURCE_EFFICIENT = "resource_efficient"
    NETWORK_EFFICIENT = "network_efficient"


class SecurityCategory(str, Enum):
    """Security classification for algorithms."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class MetricName(str, Enum):
    """Metric names tracked by QuMARA."""

    AUTH_LATENCY = "authentication_latency_ms"
    VERIFY_LATENCY = "verification_latency_ms"
    CPU_USAGE = "cpu_usage_percent"
    MEMORY_USAGE = "memory_usage_mb"
    JWT_SIZE = "jwt_size_bytes"
    SIGNATURE_SIZE = "signature_size_bytes"
    NETWORK_OVERHEAD = "network_overhead_bytes"
    SUCCESS_RATE = "success_rate"
    ERROR_RATE = "error_rate"
    THROUGHPUT = "throughput_rps"


class RewardComponent(str, Enum):
    """Components of the reward function."""

    LATENCY_REWARD = "latency_reward"
    SECURITY_REWARD = "security_reward"
    RESOURCE_REWARD = "resource_reward"
    AVAILABILITY_REWARD = "availability_reward"
    PENALTY_LATENCY = "penalty_latency"
    PENALTY_FAILURE = "penalty_failure"


class EnvironmentState(str, Enum):
    """Environment operational states."""

    HEALTHY = "healthy"
    DEGRADED = "degraded"
    OVERLOADED = "overloaded"
    FAULTY = "faulty"


@dataclass
class AlgorithmSpec:
    """Specification for a post-quantum authentication algorithm."""

    name: AuthenticationAlgorithm
    security_category: SecurityCategory
    signature_size_bytes: int
    jwt_size_bytes: int
    avg_signing_latency_ms: float
    avg_verification_latency_ms: float
    cpu_cost_percent: float
    memory_cost_mb: float
    bandwidth_cost_kbps: float


# Algorithm specifications
ALGORITHM_SPECS: Dict[AuthenticationAlgorithm, AlgorithmSpec] = {
    AuthenticationAlgorithm.ML_DSA_44: AlgorithmSpec(
        name=AuthenticationAlgorithm.ML_DSA_44,
        security_category=SecurityCategory.MEDIUM,
        signature_size_bytes=1440,
        jwt_size_bytes=1920,
        avg_signing_latency_ms=2.5,
        avg_verification_latency_ms=1.8,
        cpu_cost_percent=15,
        memory_cost_mb=32,
        bandwidth_cost_kbps=15.36,
    ),
    AuthenticationAlgorithm.ML_DSA_65: AlgorithmSpec(
        name=AuthenticationAlgorithm.ML_DSA_65,
        security_category=SecurityCategory.HIGH,
        signature_size_bytes=2044,
        jwt_size_bytes=2720,
        avg_signing_latency_ms=4.2,
        avg_verification_latency_ms=2.9,
        cpu_cost_percent=22,
        memory_cost_mb=48,
        bandwidth_cost_kbps=21.76,
    ),
    AuthenticationAlgorithm.ML_DSA_87: AlgorithmSpec(
        name=AuthenticationAlgorithm.ML_DSA_87,
        security_category=SecurityCategory.CRITICAL,
        signature_size_bytes=2420,
        jwt_size_bytes=3227,
        avg_signing_latency_ms=6.1,
        avg_verification_latency_ms=4.2,
        cpu_cost_percent=28,
        memory_cost_mb=64,
        bandwidth_cost_kbps=25.92,
    ),
    AuthenticationAlgorithm.SLH_DSA_128: AlgorithmSpec(
        name=AuthenticationAlgorithm.SLH_DSA_128,
        security_category=SecurityCategory.MEDIUM,
        signature_size_bytes=2144,
        jwt_size_bytes=2851,
        avg_signing_latency_ms=8.5,
        avg_verification_latency_ms=1.2,
        cpu_cost_percent=18,
        memory_cost_mb=40,
        bandwidth_cost_kbps=22.784,
    ),
    AuthenticationAlgorithm.SLH_DSA_192: AlgorithmSpec(
        name=AuthenticationAlgorithm.SLH_DSA_192,
        security_category=SecurityCategory.HIGH,
        signature_size_bytes=3856,
        jwt_size_bytes=5141,
        avg_signing_latency_ms=16.2,
        avg_verification_latency_ms=1.8,
        cpu_cost_percent=24,
        memory_cost_mb=56,
        bandwidth_cost_kbps=41.088,
    ),
    AuthenticationAlgorithm.SLH_DSA_256: AlgorithmSpec(
        name=AuthenticationAlgorithm.SLH_DSA_256,
        security_category=SecurityCategory.CRITICAL,
        signature_size_bytes=4432,
        jwt_size_bytes=5909,
        avg_signing_latency_ms=22.8,
        avg_verification_latency_ms=2.4,
        cpu_cost_percent=32,
        memory_cost_mb=72,
        bandwidth_cost_kbps=47.456,
    ),
}

# Intent profile weights
INTENT_WEIGHTS: Dict[IntentProfile, Dict[str, float]] = {
    IntentProfile.SECURITY_FIRST: {
        "security": 0.5,
        "latency": 0.1,
        "resource": 0.2,
        "availability": 0.2,
    },
    IntentProfile.PERFORMANCE_FIRST: {
        "security": 0.2,
        "latency": 0.5,
        "resource": 0.15,
        "availability": 0.15,
    },
    IntentProfile.BALANCED: {
        "security": 0.3,
        "latency": 0.3,
        "resource": 0.2,
        "availability": 0.2,
    },
    IntentProfile.RESOURCE_EFFICIENT: {
        "security": 0.2,
        "latency": 0.2,
        "resource": 0.4,
        "availability": 0.2,
    },
    IntentProfile.NETWORK_EFFICIENT: {
        "security": 0.2,
        "latency": 0.3,
        "resource": 0.25,
        "availability": 0.25,
    },
}

# Thresholds
THRESHOLDS = {
    "latency_threshold_ms": 100,
    "security_threshold": SecurityCategory.MEDIUM,
    "cpu_threshold_percent": 80,
    "memory_threshold_mb": 512,
    "error_threshold_percent": 5,
    "availability_threshold_percent": 95,
}

# RL Constants
RL_CONSTANTS = {
    "discount_factor": 0.99,
    "learning_rate": 0.0003,
    "epsilon_decay": 0.995,
    "epsilon_min": 0.01,
    "batch_size": 64,
    "replay_buffer_size": 100000,
    "update_frequency": 4,
    "target_update_frequency": 1000,
}

# Environment constants
ENVIRONMENT_CONSTANTS = {
    "max_steps_per_episode": 1000,
    "observation_window_size": 10,
    "action_space_size": len(AuthenticationAlgorithm),
    "observation_space_size": 15,
}

# Logging levels
LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

# Default configuration
DEFAULT_CONFIG = {
    "env": "development",
    "debug": True,
    "log_level": "INFO",
    "seed": 42,
}
