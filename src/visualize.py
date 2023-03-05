#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg') # Fix graphic error
import re
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# Fix Korea Font
import matplotlib.font_manager as fm
font_path = 'fonts/NanumGothic-Regular.ttf'
korea_font = fm.FontProperties(fname=font_path)

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# initialize keys and its values 
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
key_arr = []
val_arr = []

for k,v in items:
    key_arr.append(k)
    val_arr.append(v)

# sort arr
sorted_val, sorted_key = zip(*sorted(zip(val_arr, key_arr)))

top_10_val = sorted_val[-10:]
top_10_key = sorted_key[-10:]
top_10_val = list(top_10_val)
top_10_key = list(top_10_key)

#Change variable based on file
if re.search('.lang', args.input_path):
    plot_title = "Counting Language Code in GeoTwitter from 2020 on" + ' ' + args.key
    x_label = "Language Code"
    save_file_name = "lang_" + args.key + ".png"
else:
    plot_title = "Counting Country Code in GeoTwitter from 2020 on" + ' ' + args.key
    x_label = "Country Code"
    save_file_name = "country_" + args.key + ".png"

# bar plot
plt.bar(range(len(top_10_key)), top_10_val, color='red', tick_label=top_10_key)
plt.title(plot_title, fontproperties=korea_font)
plt.xlabel(x_label, fontproperties=korea_font)
plt.ylabel("Counts")

# Save plot as a png 
plt.savefig(save_file_name)
