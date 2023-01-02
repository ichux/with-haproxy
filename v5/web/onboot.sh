#!/bin/sh

# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit

# shellcheck disable=SC2039
# fail exit if one of your pipe command fails
set -o pipefail

# exits if any of your variables is not set
set -o nounset

cpu_count() {
python << END
import multiprocessing
print(multiprocessing.cpu_count())
END
}

requirements(){
  pip install -U pip setuptools wheel
  pip install -U `echo $(cat requirements.txt | sed 's/==.*//g' | tr '\n' ' ')`

  libraries=$(cat requirements.txt | sed 's/==.*//g' | tr '\n' '|')
  libs=$(pip list | egrep -i "$libraries" | tr -s ' ')
  listed=`echo "${libs// /==}"`

  # shellcheck disable=SC2039
  echo -e "${listed// /\\n}" | awk 'NR>2 {print $1}' > requirements.txt
}

if [ "$1" = "app" ]; then
  echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf && \
  printf "$(date +'%Y-%m-%d %T') \x1b[32mINFO\x1b[0m $(tail -n 1 /etc/sysctl.conf)\n"

  #  python3 -c 'while True: import ctypes; ctypes.CDLL(None).pause()'

  export CORES=`./onboot.sh cc`
  exec /usr/local/bin/supervisord --configuration /web/supervisord.conf
fi


if [ "$1" = "cc" ]; then
  #  %(ENV_CORES)s
  #  export CORES=`./onboot.sh cc`
  cpu_count && exit 0
fi

if [ "$1" = "requirements" ]; then
  requirements && exit 0
fi