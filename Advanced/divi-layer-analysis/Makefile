USE_DIVE_DOCKER ?= 0
ifeq ($(USE_DIVE_DOCKER),1)
	DIVE_CMD := docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock wagoodman/dive:latest
else
	DIVE_CMD := dive
endif

IMAGE_NAIVE := dive-naive:latest
IMAGE_OPTIMIZED := dive-opt:latest

.PHONY: build-naive build-opt dive-naive dive-opt clean all

build-naive:
	docker build -t $(IMAGE_NAIVE) -f Dockerfile.naive .

build-opt:
	docker build -t $(IMAGE_OPTIMIZED) -f Dockerfile.optimized .

dive-naive: build-naive
	$(DIVE_CMD) $(IMAGE_NAIVE)

dive-opt: build-opt
	$(DIVE_CMD) $(IMAGE_OPTIMIZED)

clean:
	docker rmi $(IMAGE_NAIVE) $(IMAGE_OPTIMIZED) || true

all: clean build-naive build-opt dive-naive dive-opt
