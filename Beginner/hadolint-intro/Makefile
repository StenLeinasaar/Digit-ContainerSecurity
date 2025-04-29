# Settings
HADOLINT_VERSION ?= v2.12.0
LINUX_BIN := ./bin/hadolint
LINUX_SHA256 := 3b0a7f22d8f6c1f9fa6c5e54029e320a3e5e0c1f2e24b2d28a6f6d2d2b3f5e12

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
  HADOLINT_BIN := $(LINUX_BIN)
else ifeq ($(UNAME_S),Darwin)
  HADOLINT_BIN := $(shell command -v hadolint)
endif

.PHONY: init lint clean

init:
ifeq ($(UNAME_S),Linux)
	@echo "==> Downloading Hadolint $(HADOLINT_VERSION) for Linux"
	@mkdir -p bin
	@curl -sSL \
		"https://github.com/hadolint/hadolint/releases/download/$(HADOLINT_VERSION)/hadolint-Linux-x86_64" \
		-o $(LINUX_BIN)
	@echo "==> Verifying checksum"
	@echo "$(LINUX_SHA256)  $(LINUX_BIN)" | sha256sum -c -
	@chmod +x $(LINUX_BIN)
	@echo
else ifeq ($(UNAME_S),Darwin)
	@echo "==> macOS detected"
	@if ! command -v hadolint >/dev/null 2>&1; then \
		echo "--> Installing Hadolint via Homebrew"; \
		brew install hadolint; \
	else \
		echo "--> Hadolint already installed"; \
	fi
endif

lint: init
	@echo "==> Running Hadolint"
	@$(HADOLINT_BIN) --config .hadolint.yaml Dockerfile

clean:
ifeq ($(UNAME_S),Linux)
	@rm -rf bin
	@echo "==> Cleaned up"
else ifeq ($(UNAME_S),Darwin)
	@echo "==> Nothing to clean on macOS"
endif