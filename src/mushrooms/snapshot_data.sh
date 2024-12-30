#!/usr/bin/env bash

echo "Getting Mushroom Environmental Data. Please wait 30 seconds."

# kill -1 $(cat /run/controller.pid)
sudo svc -h /service/mushrooms
sleep 30
# tail -n 13 controller_*.out
tail -n 13 /var/log/mushrooms/current | tai64nlocal | cut -d" " -f 3-
