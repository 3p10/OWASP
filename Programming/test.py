import requests, re

r = requests.session()
res = r.get('https://memoryleaks.ir/wp-login.php')

match = re.search(r'data-nonce="(\w+)"', res.text) # Search for the 'data-nonce' value in the response HTML

if match:
    print("Found nonce:", match.group(1)) # Print the extracted nonce value
else:
    print("Nonce not found")