#!/bin/bash

docker-compose -p hxy up --build -d

# clean up
docker stop haproxy_cf_base > /dev/null 2>&1 && docker rm haproxy_cf_base > /dev/null 2>&1

# connect from another image
docker run --tty -d --name hxy-haproxy_if_web3-1 --net hxy_net haproxy_if_base
docker exec -it hxy-haproxy_if_web3-1 python read_net_global.py 1
