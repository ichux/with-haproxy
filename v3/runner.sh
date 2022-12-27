#!/bin/bash

docker stop `docker ps -a | awk '{print $(NF)}' | grep hap | sed 's/==.*//g' | tr '\n' ' '` > /dev/null 2>&1;
docker rm `docker ps -a | awk '{print $(NF)}' | grep hap | sed 's/==.*//g' | tr '\n' ' '` > /dev/null 2>&1;

docker-compose -p hxy up --build -d

# clean up
docker stop haproxy_cf_base > /dev/null 2>&1 && docker rm haproxy_cf_base > /dev/null 2>&1

# connect from another image
docker run --rm -it --net hxy_net haproxy_if_base python read_net_global.py 1

# docker run --rm -it --net hxy_net haproxy_if_base python read_net_2_global.py 1
# docker run --rm -it --net hxy_net curlimages/curl:7.86.0 -I http://haproxy_if_web1:12345

docker logs -f haproxy_cf_app