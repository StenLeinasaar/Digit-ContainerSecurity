# Makefile for multi-stage-build demo

# Optionally run dive via Docker if not installed locally
USE_DIVE_DOCKER ?= 0
ifeq ($(USE_DIVE_DOCKER),1)
	DIVE_CMD := docker run --rm -it \
		-v /var/run/docker.sock:/var/run/docker.sock \
		wagoodman/dive:latest
else
	DIVE_CMD := dive
endif

IMAGE_NAIVE := naive-demo:latest
IMAGE_MULTI := multi-demo:latest
APP_SRC := .

.PHONY: build-naive build-multi history-naive history-multi dive-naive dive-multi clean all help

## Build naive single-stage image
build-naive:
	docker build -t $(IMAGE_NAIVE) -f Dockerfile.naive $(APP_SRC)

## Build multi-stage image
build-multi:
	docker build -t $(IMAGE_MULTI) -f Dockerfile.multi $(APP_SRC)

## Show layer history for naive image
history-naive: build-naive
	@echo "\n→ docker history $(IMAGE_NAIVE)\n"
	docker history $(IMAGE_NAIVE)

## Show layer history for multi-stage image
history-multi: build-multi
	@echo "\n→ docker history $(IMAGE_MULTI)\n"
	docker history $(IMAGE_MULTI)

## Inspect naive image layers with dive
dive-naive: build-naive
	@echo "\n→ Inspecting $(IMAGE_NAIVE) with dive\n"
	$(DIVE_CMD) $(IMAGE_NAIVE)

## Inspect multi-stage image layers with dive
dive-multi: build-multi
	@echo "\n→ Inspecting $(IMAGE_MULTI) with dive\n"
	$(DIVE_CMD) $(IMAGE_MULTI)

## Remove built images
clean:
	docker image rm $(IMAGE_NAIVE) $(IMAGE_MULTI) || true

## Build, history, and dive both
all: clean build-naive build-multi history-naive history-multi dive-naive dive-multi

## Help text
help:
	@echo "Usage:"
	@echo "  make build-naive       # Build naive single-stage image"
	@echo "  make build-multi       # Build multi-stage image"
	@echo "  make history-naive     # Show history of naive-demo"
	@echo "  make history-multi     # Show history of multi-demo"
	@echo "  make dive-naive        # Dive into naive-demo layers"
	@echo "  make dive-multi        # Dive into multi-demo layers"
	@echo "  make clean             # Remove images"
	@echo "  make all               # Full sequence"
	@echo "\nTo run dive via Docker without local install:"
	@echo "  make USE_DIVE_DOCKER=1 dive-naive"