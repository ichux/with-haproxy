#!/bin/bash

# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit

# exits if any of your variables is not set
set -o nounset

echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf && \
printf "$(date +'%Y-%m-%d %T') \x1b[32mINFO\x1b[0m $(tail -n 1 /etc/sysctl.conf)\n"

export CORES=`python3 -c "import multiprocessing; print(multiprocessing.cpu_count())"`
exec /usr/local/bin/supervisord --configuration /web/supervisord.conf
