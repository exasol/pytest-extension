# 1.0.0 - 2026-02-06

In this release we move the sub-project from the repository https://github.com/exasol/pytest-plugin into its own repository https://github.com/exasol/pytest-extension.

Additionally, the project now uses `python-toolbox` 5.0.0, meaning that most of the CI workflows are auto-generated (exception `slow-tests`).

## Refactoring

* #2: Updated `python-toolbox` to 5.0.0