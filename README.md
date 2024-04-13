## Scale with HAProxy
Demo scaling all sorts of apps with HAProxy

# Start up - V1
- Step 1:
 docker pull haproxy:2.7.1-bullseye && docker pull jmalloc/echo-server

- Step 2:
```shell
# ensure you are within v1 to run all these commands
cd v1

docker network create --driver=bridge pronet

docker run -d \
   --name web1 --net pronet jmalloc/echo-server
   
docker run -d \
   --name web2 --net pronet jmalloc/echo-server
   
docker run -d \
   --name web3 --net pronet jmalloc/echo-server

# haproxy docker
docker run -d \
   --name ihaproxy \
   --net pronet \
   -v $(pwd):/usr/local/etc/haproxy:ro \
   -p 8100:80 \
   -p 8200:8404 \
   haproxy:2.7.1-bullseye
```

- Step 3 - Browse (based on the ports in your .env)
> http://127.0.0.1:8100/ or http://127.0.0.1:8200/


# Start up - V2
- Step 1
```shell
# ensure you are within v2 to run all these commands
cd v2
cp .env-example .env # and change the ports in ".env" to taste
docker compose -p hxy up -d
```

- Step 2 - Browse (based on the ports in your .env)
> http://127.0.0.1:8100/ or http://127.0.0.1:8200/


#  Start up - V3
The concept is to test a global variable accessible across network.

Run
   > ./floods.sh

- Step 1
```shell

# total_cpus=$(grep ^cpu\\scores /proc/cpuinfo | uniq |  awk '{print $4}')
# echo "$total_cpus"

# ensure you are within v3 to run all these commands
cd v3
cp .env-example .env # and change the ports in ".env" to taste

docker compose -p hxy up --build -d haproxy_if_base
docker compose -p hxy up --build -d

# clean up
docker stop haproxy_cf_base > /dev/null 2>&1 && docker rm haproxy_cf_base > /dev/null 2>&1

# connect from another image
docker run --tty -d --name hxy-haproxy_if_web3-1 --net hxy_net haproxy_if_base
docker exec -it hxy-haproxy_if_web3-1 python read_net_1_global.py 1

# TODO: fix it
docker exec -it hxy-haproxy_if_web3-1 python read_net_2_global.py 1
```

#  Start up - V4
The concept is to test a global variable accessible across network.

Run
   > ./floods.sh

- Step 1
```shell

# total_cpus=$(grep ^cpu\\scores /proc/cpuinfo | uniq |  awk '{print $4}')
# echo "$total_cpus"

# ensure you are within v4 to run all these commands
cd v4
cp .env-example .env # and change the ports in ".env" to taste
./runner.sh

# load balancer - terminal 1
docker exec -it hxy-haproxy-if-web2-1 python load_balancer.py

# load balancer - terminal 2
docker exec -it hxy-haproxy-if-web1-1 python read_net_2_global.py 1
```