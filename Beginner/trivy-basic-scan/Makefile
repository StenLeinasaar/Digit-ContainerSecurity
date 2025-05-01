# Makefile for trivy-basic-scan demo on macOS

# If you prefer the Docker image, set USE_DOCKER=1
USE_DOCKER ?= 0

# Trivy command (local or dockerized)
ifeq ($(USE_DOCKER),1)
	TRIVY := docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest
else
	TRIVY := trivy
endif

.PHONY: install uninstall build-demo scan-nginx scan-ubuntu scan-demo scan-config all help

## install Trivy via Homebrew
install:
ifeq ($(USE_DOCKER),1)
	@echo "▶ Using Dockerized Trivy; no install needed."
else
	@echo "▶ Installing Trivy via Homebrew..."
	brew tap aquasecurity/trivy || true
	brew install trivy
	@echo "✔ Trivy installed."
endif

## uninstall Trivy
uninstall:
ifeq ($(USE_DOCKER),1)
	@echo "▶ Using Dockerized Trivy; nothing to uninstall."
else
	@echo "▶ Uninstalling Trivy..."
	brew uninstall trivy || true
	brew untap aquasecurity/trivy || true
	@echo "✔ Trivy removed."
endif

## build a tiny image with a known-vulnerable bash
build-demo:
	@echo "▶ Building vulnerable demo image..."
	docker build -t demo-vuln:latest -f Dockerfile.demo .

## scan nginx:alpine
scan-nginx:
	@echo "▶ Scanning nginx:alpine..."
	$(TRIVY) image nginx:alpine --format json --output $@.json

## scan ubuntu:latest
scan-ubuntu:
	@echo "▶ Scanning ubuntu:latest..."
	$(TRIVY) image ubuntu:latest --format json --output $@.json

## scan our demo image
scan-demo: build-demo
	@echo "▶ Scanning demo-vuln:latest..."
	$(TRIVY) image demo-vuln:latest --format json --output $@.json

## scan current directory for IaC/config issues
scan-config:
	@echo "▶ Scanning ./ for config-as-code issues..."
	$(TRIVY) config --severity HIGH,CRITICAL iac-demo/ --format json --output $@.json

## scan everything
all: scan-nginx scan-ubuntu scan-demo scan-config

## show help
help:
	@echo "Usage:"
	@echo "  make install           # Install Trivy"
	@echo "  make uninstall         # Remove Trivy"
	@echo "  make scan-nginx        # CVEs in nginx:alpine"
	@echo "  make scan-ubuntu       # CVEs in ubuntu:latest"
	@echo "  make scan-demo         # Build & scan demo-vuln:latest"
	@echo "  make scan-config       # IaC/config misconfigs in this dir"
	@echo "  make all               # Run all scans"
	@echo
	@echo "To use the Dockerized Trivy binary instead of Homebrew:"
	@echo "  make USE_DOCKER=1 all"
