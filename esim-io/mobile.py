import requests as session

headers = {
    "accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip",
    "Connection": "Keep-Alive",
    "Content-Length": "218",
    "Content-Type": "application/json",
    "Host": "api.esim.io",
    "user-agent": "X",
    "x-app-version": "1.0.11",
    "x-client-device-id": "6657ba21959c56d8",
    "x-currency": "USD",
    "x-lang": "en",
    "x-os": "android",
    "x-os-version": "11",
    "x-req-signature": "-1",
    "x-req-timestamp": "1735676439742"
}

data = {
    "countryCode": "US",
    "timeZone": "Europe/Oslo",
    "deviceName": "r0qxxx",
    "peerKey": "1",
    "notificationToken": "1234567asdfghjk...",
    "carrierName": "Taiwan Mobile",
    "carrierCountryCode": "tw",
    "carrierNetworkCode": "97",
    "oldToken": ""
}

response = session.post('https://api.esim.io/init', headers=headers, json=data)
token = response.json()["result"]["token"]

headers = {
    "accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip",
    "Connection": "Keep-Alive",
    "Content-Type": "application/json",
    "Host": "api.esim.io",
    "user-agent": "X",
    "x-app-version": "1.0.11",
    "x-client-device-id": "6657ba21959c56d8",
    "x-currency": "USD",
    "x-lang": "en",
    "x-os": "android",
    "x-os-version": "11",
    "x-req-signature": "R0XzSzggXCsBSmFFG7H5Oc/eAtn0KwsRCr8ZHqhaYmc=",
    "x-req-timestamp": "1735676470390",
    "x-token": "W8O-kaakt0M8cQZYIFTfi1CIMKhxLuj-YvpysitGZcE80ByubBXOBNcChZo9Gfkw"
}

data = {
    "email": "..."
}

response = session.post('https://api.esim.io/auth/send-email', headers=headers, json=data)

print(response.text)