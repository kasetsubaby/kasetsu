TAG := $(if $(filter $(shell uname), Darwin),$(shell cat Dockerfile cpanfile.snapshot | md5),$(shell cat Dockerfile cpanfile.snapshot | md5sum | cut -d' ' -f1))

build:
	docker build -t kasetsu:$(TAG) .

run:
	@make build
	@docker run -it -d \
		-v $(shell pwd):/usr/local/projects/kasetsu \
		-p 15000:5000 \
		--name kasetsu kasetsu:$(TAG)

clean:
	@docker stop kasetsu \
		&& docker rm kasetsu \
		&& docker rmi kasetsu:$(TAG)
