# get relevant information from json file
# TO RUN
# python json_read.py < 7songs.txt

import sys, re

for line in sys.stdin:
    if ":track:" in line:
        line = line.strip()
        line = line.replace(r'"uri": "', '')
        line = line.replace(r'",', '')
        line = line.replace(r'spotify:track:','')
        print line
