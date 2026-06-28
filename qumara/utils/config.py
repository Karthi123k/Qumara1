"""Configuration management for QuMARA.

Provides centralized configuration loading from YAML files.
"""

import os
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from qumara.utils.exceptions import ConfigurationException
from qumara.utils.logger import Logger

logger = Logger.get_logger(__name__)


class ConfigLoader:
    """Load and manage YAML configuration files."""

    _cache: Dict[str, Any] = {}
    _base_dir: Path = Path(__file__).parent.parent.parent / "config"

    @classmethod
    def set_base_dir(cls, base_dir: str) -> None:
        """Set base directory for configuration files.

        Args:
            base_dir: Path to configuration directory
        """
        cls._base_dir = Path(base_dir)
        if not cls._base_dir.exists():
            raise ConfigurationException(f"Config directory not found: {cls._base_dir}")

    @classmethod
    def load(cls, config_file: str, use_cache: bool = True) -> Dict[str, Any]:
        """Load configuration from YAML file.

        Args:
            config_file: Configuration file name or path
            use_cache: Whether to use cached configuration

        Returns:
            Configuration dictionary

        Raises:
            ConfigurationException: If file not found or parsing fails
        """
        if use_cache and config_file in cls._cache:
            logger.debug(f"Using cached configuration: {config_file}")
            return cls._cache[config_file]

        config_path = cls._base_dir / config_file
        if not config_path.exists():
            raise ConfigurationException(f"Configuration file not found: {config_path}")

        try:
            with open(config_path, "r") as f:
                config = yaml.safe_load(f) or {}
            logger.info(f"Loaded configuration from {config_path}")
            cls._cache[config_file] = config
            return config
        except yaml.YAMLError as e:
            raise ConfigurationException(f"Invalid YAML in {config_path}: {e}")
        except Exception as e:
            raise ConfigurationException(f"Failed to load {config_path}: {e}")

    @classmethod
    def load_with_env(cls, config_file: str) -> Dict[str, Any]:
        """Load configuration and override with environment variables.

        Environment variables should be prefixed with 'QUMARA_'
        and use double underscores for nested keys.
        Example: QUMARA_SERVICE_PORT=8001

        Args:
            config_file: Configuration file name

        Returns:
            Configuration dictionary with environment overrides
        """
        config = cls.load(config_file)
        prefix = "QUMARA_"

        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix) :].lower()
                config[config_key] = value
                logger.debug(f"Overriding config {config_key} from environment")

        return config

    @classmethod
    def get(cls, config_file: str, key: str, default: Any = None) -> Any:
        """Get a specific configuration value.

        Args:
            config_file: Configuration file name
            key: Configuration key (supports dot notation for nested keys)
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        config = cls.load(config_file)
        keys = key.split(".")
        value = config

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default

        return value if value is not None else default

    @classmethod
    def clear_cache(cls) -> None:
        """Clear configuration cache."""
        cls._cache.clear()
        logger.debug("Configuration cache cleared")
