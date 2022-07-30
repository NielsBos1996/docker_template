SHELL := /bin/bash

.PHONY: help
help:
	@echo "todo"

.PHONY: start
start:
	docker-compose up --build --remove-orphans

.PHONY: stop
stop:
	docker-compose down -v
