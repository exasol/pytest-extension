"""Configuration for nox based task runner"""

from __future__ import annotations

from collections.abc import (
    MutableMapping,
)
from pathlib import Path
from typing import (
    Any,
)

from exasol.toolbox.config import BaseConfig
from exasol.toolbox.util.version import Version
from nox import Session
from pydantic import computed_field


class Config(BaseConfig):
    """Project-specific configuration used by nox infrastructure"""

    @computed_field  # type: ignore[misc]
    @property
    def extended_python_versions(self) -> list[str]:
        """
        Lowest and highest versions from ``python_versions``.

        Used by the slow-checks workflow to run expensive integration tests
        against only the two extreme Python versions instead of the full
        matrix.
        """
        versions = sorted(self.python_versions, key=Version.from_string)
        return sorted({versions[0], versions[-1]}, key=Version.from_string)

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
    python_versions=("3.10", "3.11", "3.12", "3.13", "3.14"),
    # Uses SaaS; not ITDE DB versions
    exasol_versions=(),
)
