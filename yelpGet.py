from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from random import shuffle

def init_client():
    auth = Oauth1Authenticator(
        consumer_key='qKDAmYD3oBrbtpPxwayMlA',
        consumer_secret='p4CmJcPczkwZuXYGgu1bIUXOD84',
        token='tzlULK4Ma3t6YLBs-Duh4HlTHtc0th0_',
        token_secret='QRX7Zz2TWCtUf-JBt5QYbtg87wc'
    )

    client = Client(auth)
    return client


def define_parameters():
    kwargs = {
        'distance': 1600,
        'term' : 'Coffee',
        'sort' : 2
    }
    return kwargs


def search(client):
    search_results = client.search_by_coordinates(42.3539305,-71.05898, **kwargs)
    return search_results

list = []
client = init_client()
kwargs = define_parameters()
results = search(client)
for business in results.businesses:
    list.append(business)

shuffle(list)
print list[0].name
"""
The way you would run this code would be:
1. Command line: pip install yelp

import yelpGet

client = init_client()
kwargs = define_parameters()
results = search(client)

for business in results.businesses:
    print business.name
"""