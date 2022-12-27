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
docker-compose -p hxy up -d
```

- Step 2 - Browse (based on the ports in your .env)
> http://127.0.0.1:8100/ or http://127.0.0.1:8200/


#  Start up - V3
The concept is to test a global variable accessible across network.

Assumptions
1. The virtual environment is activated
2. You have started the server on a separate shell
   > python web/external/share_global.py
3. Run 1000 concurrent requests using bash.
   > ./floods.sh

- Step 1
```shell
# ensure you are within v3 to run all these commands
cd v3
cp .env-example .env # and change the ports in ".env" to taste
docker-compose -p hxy up -d
```