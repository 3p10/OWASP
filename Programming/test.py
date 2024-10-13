import requests, re

r = requests.session()
res = r.get('https://memoryleaks.ir/wp-login.php')

match = re.search(r'data-nonce="(\w+)"', res.text)

if match:
    print("Found nonce:", match.group(1))
else:
    print("Nonce not found")