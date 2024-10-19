import requests, json

r = requests.session()

phone_number = input("Enter your phone number: ")
print(f'You entered: {phone_number}')

if phone_number:
    data = {
    "username": phone_number,
    "otp_call": False
    }
    headers = {
        "Content-Type": "application/json"
    }

    #Send the POST request 
    res = r.post('https://api.digikala.com/v1/user/authenticate/', headers=headers, data=json.dumps(data))

    if res.json().get("status") == 200:
        print("[+] SMS has been sent.")
        otp_code = input("Enter OTP code: ")
        
    else:
        print(f'[-] Error: {res.text}')
