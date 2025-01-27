#!/usr/bin/bash

###   Start Mushroom Environmental Control via daemonize

#__author__ = "Matt Martini"
#__email__ = "matt.martini@imaginarywave.com"
#__version__ = "0.3.0"


dir='/home/martini/MusroomHouse/src/mushrooms/'
envdir='/home/martini/MushroomHouse/service/env'
cmd='controller'

date=$(date "+%Y%m%d_%H%M%S")

/usr/bin/daemonize -a -v \
                          -c ${dir} \
                          -e ${dir}/${cmd}_${date}.err \
                          -o ${dir}/${cmd}_${date}.out \
                          -p /run/${cmd}.pid \
                          -l /run/lock/${cmd}.lock \
                          -E BUCKET_NAME="$(cat ${envdir}/BUCKET_NAME)" \
                          -E BUCKET_KEY="$(cat ${envdir}/BUCKET_KEY)" \
                          -E ACCESS_KEY="$(cat ${envdir}/ACCESS_KEY)" \
                          -u martini python ${dir}/${cmd}.py

