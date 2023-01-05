# Supervisor API calls
```shell
docker exec -it cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.system.methodHelp('supervisor.shutdown'))"

docker exec -it cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.supervisor.getState())"

docker exec -it cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.system.listMethods())"

docker exec -it cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.supervisor.getProcessInfo('data_science:1001'))"

docker exec -it cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.supervisor.signalAllProcesses('data_science'))"
```

# Run app
> docker exec -it cds python3 read_global.py 10