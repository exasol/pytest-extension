# 1.1.0 - 2026-06-25

## Summary

Added support for Python3.14

## Security Issues

This release fixes vulnerabilities by updating dependencies:

| Dependency | Vulnerability | Affected | Fixed in |
|------------|---------------|----------|----------|
| cryptography | GHSA-537c-gmf6-5ccf | 48.0.0 | 48.0.1 |
| gitpython | GHSA-mv93-w799-cj2w | 3.1.49 | 3.1.50 |
| idna | PYSEC-2026-215 | 3.11 | 3.15 |
| msgpack | GHSA-6v7p-g79w-8964 | 1.1.2 | 1.2.1 |
| pip | PYSEC-2026-196 | 26.1.1 | 26.1.2 |
| tornado | CVE-2026-49854 | 6.5.5 | 6.5.6 |
| tornado | CVE-2026-49853 | 6.5.5 | 6.5.6 |
| tornado | CVE-2026-49855 | 6.5.5 | 6.5.6 |
| tornado | GHSA-pw6j-qg29-8w7f | 6.5.5 | 6.5.7 |
| urllib3 | PYSEC-2026-142 | 2.6.3 | 2.7.0 |
| urllib3 | PYSEC-2026-142 | 2.6.3 | 2.7.0 |
| urllib3 | PYSEC-2026-141 | 2.6.3 | 2.7.0 |

## Refactoring

* #22: Updated to `exasol-toolbox` 8.1.1
* #26: Updated to `exasol-toolbox` 10.0.0
* #28: Added support for Python3.14

## Dependency Updates

### `main`

* Updated dependency `exasol-python-extension-common:0.13.0` to `0.16.0`
* Updated dependency `pyexasol:2.2.1` to `2.2.2`
* Updated dependency `pytest:9.0.3` to `9.1.1`
* Updated dependency `pytest-exasol-backend:1.4.1` to `1.5.0`

### `dev`

* Updated dependency `click:8.2.1` to `8.4.2`
* Updated dependency `exasol-toolbox:7.0.0` to `10.0.0`