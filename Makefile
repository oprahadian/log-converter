build:
	docker build -t log-converter .

help:
	docker run -it -v "$PWD":/usr/src/app -w /usr/src/app --rm log-converter --help