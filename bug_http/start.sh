#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# 1. Kill the running backend and frontend (ignore errors if they are not running):
sudo killall -9 python3 2>/dev/null

# 2. Start the backend server:
cd $DIR
sudo rm -f nohup.out
date > nohup.out
sudo nohup python3 -u server.py 9000 &
sudo nohup nice -n -5 python3 -u -m http.server 8000 &

sudo less nohup.out
