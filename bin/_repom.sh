#!/bin/bash

SCRIPT=`which _repom.sh`
ROOT="$( cd "$( dirname "$SCRIPT" )" && pwd )"
`$ROOT/_repom.py $@`

