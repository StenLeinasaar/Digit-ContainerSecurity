# Hadolint Introduction Demo

This demo shows how to install and run **Hadolint** locally via a `Makefile`. It also verifies the integrity of the downloaded binary.

## Prerequisites
- GNU Make
- `curl`, `sha256sum`

## Files

- `Dockerfile`: Example with common bad practices.
- `.hadolint.yaml`: Linting configuration.
- `Makefile`: Tasks for downloading, verifying, and running Hadolint.

## Usage

1. **Initialize**:
   ```bash
   make init



brew install hadolint
hadolint --config .hadolint.yaml Dockerfile