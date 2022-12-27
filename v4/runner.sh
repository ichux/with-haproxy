#!/bin/bash

docker stop `docker ps -a | awk '{print $(NF)}' | grep hap | sed 's/==.*//g' | tr '\n' ' '` > /dev/null 2>&1;
docker rm `docker ps -a | awk '{print $(NF)}' | grep hap | sed 's/==.*//g' | tr '\n' ' '` > /dev/null 2>&1;

docker-compose -p hxy up --build -d

docker exec -it hxy-haproxy-if-web1-1 python read_net_global.py 5

docker logs -f hxy-haproxy-if-web1-1