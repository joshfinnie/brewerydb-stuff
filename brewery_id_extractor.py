#!/usr/local/bin/python
import sys

import requests

url = "http://api.brewerydb.com/v2/breweries/?key={}&p={}"

brewery_ids = []
for i in range(0, 118):
    r = requests.get(url.format(sys.argv[1], i))
    data = r.json()
    breweries = data['data']
    for brewery in breweries:
        brewery_ids.append(brewery['id'])

print brewery_ids
