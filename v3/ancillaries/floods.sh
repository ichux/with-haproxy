#!/bin/bash

eval "
$(cat <<EOF
for i in {1..100}; do echo 'python read_global.py 100'; done
EOF
)" | xargs -P 20 -I {} sh -c 'printf "`$1`"' - {}
