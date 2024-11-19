import requests

r = requests.session()
response = r.get('https://wordlists.assetnote.io/data/automated.json')

for item in response.json().get('data'): # Loop through each item in the 'data' field of the JSON response
    print('https://wordlists-cdn.assetnote.io/./data/automated/' + item['Filename'])