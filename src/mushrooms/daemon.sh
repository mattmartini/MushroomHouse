#!/usr/bin/bash

###   Start Mushroom Environmental Control via daemonize

#__author__ = "Matt Martini"
#__email__ = "matt.martini@imaginarywave.com"
#__version__ = "0.3.0"


dir='/home/martini/MusroomHouse/src/mushrooms/'
cmd='controller'

date=$(date "+%Y%m%d_%H%M%S")

/usr/local/sbin/daemonize -a -v \
                          -c ${dir} \
                          -e ${dir}/${cmd}_${date}.err \
                          -o ${dir}/${cmd}_${date}.out \
                          -p /run/${cmd}.pid \
                          -l /run/lock/${cmd}.lock \
                          -E BUCKET_NAME=$(cat ${dir}/../../service/env/BUCKET_NAME) \
                          -E BUCKET_KEY=$(cat ${dir}/../../service/env/BUCKET_KEY) \
                          -E ACCESS_KEY=$(cat ${dir}/../../service/env/ACCESS_KEY) \
                          -u pi /usr/bin/python3  ${dir}/${cmd}.py

