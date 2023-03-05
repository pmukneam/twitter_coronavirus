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
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

key_arr = []
val_arr = []

for k,v in items:
    # print(k,':',v)
    key_arr.append(k)
    val_arr.append(v)

# sort arr
sorted_val, sorted_key = zip(*sorted(zip(val_arr, key_arr)))

top_10_val = sorted_val[-10:]
top_10_key = sorted_key[-10:]

top_10_val = list(top_10_val)
top_10_key = list(top_10_key)

print(top_10_val)
print(top_10_key)

temp = range(len(top_10_key))

plt.bar(temp, top_10_val, color='red', tick_label=top_10_key)

#plt.xticks(temp, top_10_key)

plt.savefig('test2.png')
"""
import pandas as pd

# create a sample DataFrame
data = {'name': list(top_10_key),
        'value': list(top_10_val)}
df = pd.DataFrame(data)

# sort the DataFrame by 'value' in descending order
df_sorted = df.sort_values('value', ascending=True)

# plot the bar chart
plt.bar(df_sorted['name'], df_sorted['value'])

# add axis labels and title
plt.xlabel('Name')
plt.ylabel('Value')
plt.title('Sorted Bar Chart')

# show the plot
plt.show()
"""
"""

# plot bar graph
plt.bar(positions, sorted(list(top_10_val)))
# plt.barh

# replace axis label
plt.xticks(positions, list(top_10_key))

plt.title('My Bar Graph')

plt.xlabel('key')
plt.ylabel('count')

plt.tight_layout()
plt.savefig('test.png')

"""
