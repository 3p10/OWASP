import requests
from bs4 import BeautifulSoup

r = requests.session()

res = r.get('https://memoryleaks.ir/wp-login.php')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')

# Find the div tag with the class 'c4wp_captcha_field' and extract the data-nonce attribute
div_tag = soup.find('div', class_='c4wp_captcha_field')

if div_tag:
    data_nonce = div_tag.get('data-nonce')
    print("data-nonce:", data_nonce)
else:
    print("No div with the specified class found.")