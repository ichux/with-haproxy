# Do not remove this block. It is used by the 'help' rule when
# constructing the help output.
# help:
# help: nginx docker socker help
# help:

.PHONY: help
# help: help				- Please use "make <target>" where <target> is one of
help:
	@grep "^# help\:" Makefile | sed 's/\# help\: //' | sed 's/\# help\://'

.PHONY: 0
# help: 0 				- build main image
0:
	@docker-compose -p onsocket up --build -d
