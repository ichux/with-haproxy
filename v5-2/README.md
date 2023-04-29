# How to Run/Use App
```shell

# build app
make 0

# run with developed benchmarks
make 1

# run with 10 readers/workers
make 2

# run 50 concurrent requests with each running 100 workers
make 3

# control your readers/workers
docker exec -i cds python3 read_global.py 50

# try ordinary benchmarks
# this might fail if it's not Python 3.10 'Passing coroutines is forbidden, use tasks explicitly.''
python3.10 web/benchmark.py
python3.10 web/benchmark_2.py
python3.10 web/benchmark_3.py


# Supervisor API calls
```shell
docker exec -i cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.supervisor.getState())"

docker exec -i cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.system.listMethods())"

docker exec -i cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.supervisor.getProcessInfo('data_science:1001'))"

docker exec -i cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.supervisor.signalAllProcesses('data_science'))"

docker exec -i cds python3 -c "from xmlrpc.client import ServerProxy;\
server = ServerProxy('http://admin:d5a122d9@localhost:9001/RPC2');\
print(server.system.methodHelp('supervisor.shutdown'))"
```
