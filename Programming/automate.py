import requests, json, urllib3 #type: ignore

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print('''
 ____  _       _ _         _         _             _                       
|  _ \(_) __ _(_) | ____ _| | __ _  | | ___   __ _(_)_ __         ___ _ __ 
| | | | |/ _ | | |/ / _ | |/ _ | | |/ _ \ / _ | | '_ \ _____ / _ \ '__|
| |_| | | (_| | |   < (_| | | (_| | | | (_) | (_| | | | | |_____|  __/ |   
|____/|_|\__, |_|_|\_\__,_|_|\__,_| |_|\___/ \__, |_|_| |_|      \___|_|   
         |___/                               |___/                        
''')

r = requests.session()

#Set proxies
proxies = {
    "http": "http://172.31.32.1:80",
    "https": "http://172.31.32.1:80",
}
r.proxies.update(proxies)
r.verify = False

#phone number → HTTP 
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

    #OTP → HTTP (login)
    if res.json().get("status") == 200:
        print("[+] SMS has been sent.")
        otp_code = input("Enter OTP code: ")

        data = {
            "type": "otp",
            "username": phone_number,
            "code": otp_code
        }
        res = r.post('https://api.digikala.com/v1/user/login/otp/', headers=headers, data=json.dumps(data))
        
        #GET user profile → HTTP (data)
        if res.json().get("status") == 200:
            res = r.get('https://api.digikala.com/v1/user/init/')
            user_data = res.json().get('data').get('user')

            print(f'user id: {user_data["id"]}')
            print(f'user first_name: {user_data["first_name"]}')
            print(f'user last_name: {user_data["last_name"]}')
        else:
            print(f'[-] Error: {res.text}')

    else:
        print(f'[-] Error: {res.text}')