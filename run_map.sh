#!/bin/sh

# loop all files in the /data/Twitter\ dataset
for zip in /data/Twitter\ dataset/geoTwitter2*; do
    # run map.py on each zip file
    nohup ./src/map.py --input_path="$zip" &
done
