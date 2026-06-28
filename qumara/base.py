"""Abstract base classes for QuMARA."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Optional

from qumara.models import TelemetryRecord


class AuthenticationAgent(ABC):
    """Base class for authentication agents."""

    @abstractmethod
    def authenticate(self, credentials: Dict[str, Any]) -> str:
        """Authenticate user and return JWT.

        Args:
            credentials: User credentials

        Returns:
            JWT token
        """
        pass

    @abstractmethod
    def verify(self, token: str) -> Dict[str, Any]:
        """Verify JWT token.

        Args:
            token: JWT token

        Returns:
            Token claims
        """
        pass


class RLAgent(ABC):
    """Base class for RL agents."""

    @abstractmethod
    def select_action(self, observation: Any) -> int:
        """Select action based on observation.

        Args:
            observation: Environment observation

        Returns:
            Action index
        """
        pass

    @abstractmethod
    def learn(self, observation: Any, action: int, reward: float, next_observation: Any) -> None:
        """Learn from experience.

        Args:
            observation: Current observation
            action: Action taken
            reward: Reward received
            next_observation: Next observation
        """
        pass


class Environment(ABC):
    """Base class for RL environments."""

    @abstractmethod
    def reset(self) -> Any:
        """Reset environment.

        Returns:
            Initial observation
        """
        pass

    @abstractmethod
    def step(self, action: int) -> tuple:
        """Execute action in environment.

        Args:
            action: Action to execute

        Returns:
            Tuple of (observation, reward, done, info)
        """
        pass


class TelemetryCollector(ABC):
    """Base class for telemetry collection."""

    @abstractmethod
    def collect(self, record: TelemetryRecord) -> None:
        """Collect telemetry record.

        Args:
            record: Telemetry record
        """
        pass

    @abstractmethod
    def export(self, format: str = "csv") -> str:
        """Export collected telemetry.

        Args:
            format: Export format (csv, json, parquet)

        Returns:
            Export file path
        """
        pass


class AuthenticationPolicy(ABC):
    """Base class for authentication policies."""

    @abstractmethod
    def get_algorithm(self) -> str:
        """Get selected algorithm name.

        Returns:
            Algorithm name
        """
        pass

    @abstractmethod
    def get_parameters(self) -> Dict[str, Any]:
        """Get algorithm parameters.

        Returns:
            Algorithm parameters
        """
        pass


class IntentEngine(ABC):
    """Base class for intent engines."""

    @abstractmethod
    def select_policy(self, intent: str, metrics: Dict[str, float]) -> str:
        """Select authentication policy based on intent.

        Args:
            intent: Intent profile name
            metrics: Current system metrics

        Returns:
            Selected algorithm name
        """
        pass


class RewardFunction(ABC):
    """Base class for reward functions."""

    @abstractmethod
    def calculate(self, metrics: Dict[str, float], intent: str) -> float:
        """Calculate reward based on metrics and intent.

        Args:
            metrics: System metrics
            intent: Intent profile

        Returns:
            Reward value
        """
        pass
