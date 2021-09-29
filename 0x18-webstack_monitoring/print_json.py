#!/usr/bin/python3
import json
import pprint
import sys

print(sys.argv[1])

with open(sys.argv[1]) as file:
    data = json.load(file)

pprint.pprint(data)

