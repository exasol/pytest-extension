"""Configuration for nox based task runner"""

from __future__ import annotations

from collections.abc import (
    Iterable,
    MutableMapping,
)
from pathlib import Path
from typing import (
    Any,
)

from exasol.toolbox.config import BaseConfig
from nox import Session


class Config(BaseConfig):
    """Project-specific configuration used by nox infrastructure"""

    @staticmethod
    def pre_integration_tests_hook(
        _session: Session, _config: Config, _context: MutableMapping[str, Any]
    ) -> bool:
        """Implement if project-specific behavior is required"""
        return True

    @staticmethod
    def post_integration_tests_hook(
        _session: Session, _config: Config, _context: MutableMapping[str, Any]
    ) -> bool:
        """Implement if project-specific behavior is required"""
        return True


PROJECT_CONFIG = Config(
    root_path=Path(__file__).parent,
    project_name="pytest_extension",
    python_versions=("3.10", "3.11", "3.12", "3.13"),
    # Uses SaaS; not ITDE DB versions
    exasol_versions=(),
)
