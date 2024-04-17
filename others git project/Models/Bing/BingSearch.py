
#Copyright (c) Microsoft Corporation. All rights reserved.
#Licensed under the MIT License.

# -*- coding: utf-8 -*-

import json
import os 
from pprint import pprint
import requests
from configparser import ConfigParser
import httpx


'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''


# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscription_key = '4f1f5655305741acb573445385162f36'
endpoint = 'https://api.bing.microsoft.com/' + '/v7.0/search'

config = ConfigParser()
config.read('credentials.ini')
# api_key = config['BingAPI']['api_key']
# web_search_endpoint = "https://api.bing.microsoft.com/v7.0/search"


headers = {'Ocp-Apim-Subscription-Key': subscription_key}


query = 'cyberpunk'
# Query term(s) to search for. 
params = {
    'q': query,
    'count': 50,
    'offset': 0,
    'mkt': 'en-US',
    'freshness': 'Month',
}

try:
    response = httpx.get(endpoint, headers=headers, params=params)
    response.raise_for_status()  # Raise an exception if the request failed

    # Process the response if successful

except httpx.HTTPError as error:
    print(f"An HTTP error occurred: {error}")
except Exception as error:
    print(f"Another error occurred: {error}")

print(response.json)
search_results = response.json()
# Example accessing 'webPages' from the results, assuming correct response structure

web_pages = search_results.get('webPages', {}).get('value', []) 

for page in web_pages:
    print(f"Title: {page['name']}")
    print(f"URL: {page['url']}")
    # ... and so on 


# # Construct a request
# mkt = 'en-US'
# params = { 'q': query, 'mkt': mkt }
# headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

# # Call the API
# try:
#     response = requests.get(endpoint, headers=headers, params=params)
#     response.raise_for_status()

#     print("Headers:")
#     print(response.headers)

#     print("JSON Response:")
#     pprint(response.json())
# except Exception as ex:
#     raise ex
    