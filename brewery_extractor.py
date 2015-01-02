#!/usr/local/bin/python
import datetime
import sys

import requests

url = "http://api.brewerydb.com/v2/brewery/{}?key={}&withSocialAccounts=Y&withLocations=Y"

r = requests.get(url.format(sys.argv[1], sys.argv[2]))
data = r.json()
data = data['data']

output = {}

output['brewerydb_id'] = data['id']
output['name'] = data.get('name', '')
output['website'] = data.get('website', '')
output['image'] = data.get('images', {'large': ''})['large']
social_accounts = data.get('socialAccounts', None)
if social_accounts:
    for account in social_accounts:
        if account['socialMedia']['name'] == "Facebook Fan Page":
            output['facebook_handle'] = account['handle']
            output['facebook_link'] = account['link']
        if account['socialMedia']['name'] == "Twitter":
            output['twitter_handle'] = account['handle']
            output['twitter_link'] = account['link']
output['location'] ={}
locations = data.get('locations', None)
if locations:
    for location in locations:
        if location['isPrimary'] == 'Y':
            output['location']['street'] = location['streetAddress']
            output['location']['locality'] = location['locality']
            output['location']['region'] = location['region']
            output['location']['postal_code'] = location['postalCode']
            output['location']['lat'] = location['latitude']
            output['location']['lon'] = location['longitude']
output['created_on'] = datetime.datetime.now()
output['last_updated_on'] = datetime.datetime.now()

print output
