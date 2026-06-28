"""Custom exception classes for QuMARA."""


class QuMARAException(Exception):
    """Base exception for QuMARA."""

    pass


class AuthenticationException(QuMARAException):
    """Raised when authentication fails."""

    pass


class ConfigurationException(QuMARAException):
    """Raised when configuration is invalid."""

    pass


class EnvironmentException(QuMARAException):
    """Raised when environment setup fails."""

    pass


class TrainingException(QuMARAException):
    """Raised when training fails."""

    pass


class EvaluationException(QuMARAException):
    """Raised when evaluation fails."""

    pass


class TokenException(QuMARAException):
    """Raised when JWT token operations fail."""

    pass


class PolicyException(QuMARAException):
    """Raised when policy operations fail."""

    pass


class TelemetryException(QuMARAException):
    """Raised when telemetry collection fails."""

    pass
