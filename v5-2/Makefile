# Do not remove this block. It is used by the 'help' rule when
# constructing the help output.
# help:
# help: nginx docker socker help
# help:

.PHONY: help
# help: help				- Please use "make <target>" where <target> is one of
help:
	@grep "^# help\:" Makefile | sed 's/\# help\: //' | sed 's/\# help\://'

.PHONY: a
# help: a 				- build apache airflow image
a:
	@#echo -e "AIRFLOW_UID=$(id -u)" > .env
	@docker-compose -f airflow-docker-compose.yml up --build -d

.PHONY: 0
# help: 0 				- build main image
0:
	@docker-compose up --build -d

.PHONY: 1
# help: 1 				- try with ordinary benchmarks
1:
	@docker exec -i cds python3 benchmark.py
	@docker exec -i cds python3 benchmark_2.py
	@docker exec -i cds python3 benchmark_3.py

.PHONY: 2
# help: 2 				- try with 10 runs
2:
	@docker exec -i cds python3 read_global.py 10

.PHONY: 3
# help: 3 				- try with 50 concurrent requests with each running 100 workers
3:
	@seq 1 50 | xargs -n1 -P50 docker exec -i cds python3 read_global.py 100
