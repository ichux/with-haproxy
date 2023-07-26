# Do not remove this block. It is used by the 'help' rule when
# constructing the help output.
# help:
# help: base64 Makefile help
# help:

UNAME := $(shell uname)

.PHONY: help
# help: help				- Please use "make <target>" where <target> is one of
help:
	@grep "^# help\:" Makefile | sed 's/\# help\: //' | sed 's/\# help\://'

.PHONY: ba
# help: ba				- build application
ba:
	@docker compose -f docker-compose.yml up --build -d
