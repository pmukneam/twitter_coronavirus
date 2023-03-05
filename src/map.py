#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--output_folder',default='outputs_broken_dates')
args = parser.parse_args()

# imports
import os
import zipfile
import datetime 
import json
from collections import Counter,defaultdict

# load keywords
hashtags = [
    '#코로나바이러스',  # korean
    '#コロナウイルス',  # japanese
    '#冠状病毒',        # chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
    ]

# initialize counters
counter_lang = defaultdict(lambda: Counter())
counter_country = defaultdict(lambda: Counter())

# open the zipfile
with zipfile.ZipFile(args.input_path) as archive:

    # loop over every file within the zip file
    for i,filename in enumerate(archive.namelist()):
        print(datetime.datetime.now(),args.input_path,filename)

        # open the inner file
        with archive.open(filename) as f:

            # loop over each line in the inner file
            for line in f:
                
                tweet = json.loads(line)
                
                # convert text to lower case
                text = tweet['text'].lower()

                # search hashtags
                # IDEA:
                #      - check key by if key_name in dict_name
                #      - remember tweet['place'] is also a dict, need to enter 2 key
                #      - also ignore the one with empty country code
                #      - check if 'place' key even exist
                #      - edit output too

                for hashtag in hashtags:
                    lang = tweet['lang']
                    if hashtag in text:
                        # search country
                        if tweet is not None:
                            if 'place' in tweet:
                                place = tweet['place']
                                if place is not None:
                                    if 'country_code' in place:
                                        if len(place['country_code']) != 0:
                                            country = place['country_code']
                                            counter_country[hashtag][country] += 1
                                            counter_country['_all'][country] += 1 
                            counter_lang[hashtag][lang] += 1
                    counter_lang['_all'][lang] += 1
                
# open the outputfile
try:
    os.makedirs(args.output_folder)
except FileExistsError:
    pass
output_path_base = os.path.join(args.output_folder,os.path.basename(args.input_path))

output_path_lang = output_path_base+'.lang'
output_path_country = output_path_base+'.country'
print('saving',output_path_lang)
print('saving',output_path_country)
with open(output_path_lang,'w') as f:
    f.write(json.dumps(counter_lang))
with open(output_path_country,'w') as f:
    f.write(json.dumps(counter_country))
