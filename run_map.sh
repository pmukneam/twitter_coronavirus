#!/bin/sh

# loop all geoTwitter in 2020
for zip in /data/Twitter\ dataset/geoTwitter20*; do
    # run map.py on each zip file
    nohup ./src/map.py --input_path="$zip" &
done
