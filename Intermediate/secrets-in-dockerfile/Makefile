# Makefile for secrets-in-dockerfile demo

IMAGE_NAME := secret-demo:latest
EXPORT_DIR := exported_layers


# Optionally run dive via Docker if not installed locally
USE_DIVE_DOCKER ?= 0

ifeq ($(USE_DIVE_DOCKER),1)
	DIVE_CMD := docker run --rm -it \
		-v /var/run/docker.sock:/var/run/docker.sock \
		wagoodman/dive:latest
else
	DIVE_CMD := dive
endif


.PHONY: build history save dive clean all help

install:
ifeq ($(USE_DOCKER),1)
	@echo "▶ Using Dockerized dive; no install needed."
else
	@echo "▶ Installing dive via Homebrew..."
	brew install dive
	@echo "✔ dive installed."
endif
## Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

## Show layer history (reveals the ENV line)
history: build
	@echo "\n→ docker history $(IMAGE_NAME)\n"
	docker history $(IMAGE_NAME)

## Save image and extract all layers into ./exported_layers/
save: build
	@echo "\n→ Saving image and extracting layers to $(EXPORT_DIR)/\n"
	mkdir -p $(EXPORT_DIR)
	docker save $(IMAGE_NAME) | tar -x -C $(EXPORT_DIR)
	@echo "Done. Inspect files under $(EXPORT_DIR)/ to see raw layer.tar files."

## Launch docker-dive for interactive layer inspection
dive: build
	@echo "\n→ Launching docker-dive on $(IMAGE_NAME)\n"
	$(DIVE_CMD) $(IMAGE_NAME)

## Clean up exported files
clean:
	rm -rf $(EXPORT_DIR)
	docker image rm $(IMAGE_NAME) || true

## Run everything in sequence
all: clean build history save dive

## Help text
help:
	@echo "Usage:"
	@echo "  make build    # Build the demo image"
	@echo "  make history  # Show image layer history"
	@echo "  make save     # Save & extract layers to disk"
	@echo "  make dive     # Inspect image with docker-dive"
	@echo "  make clean    # Remove image & exported layers"
	@echo "  make all      # clean + build + history + save + dive"
