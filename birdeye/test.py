import tls_client

session = tls_client.Session(client_identifier="chrome_116")

import requests

url = "https://multichain-api.birdeye.so/cex/top_market"

querystring = {"time_frame":"24h","network":"solana"}

headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9,no;q=0.8",
    "agent-id": "03a8cc0f-6b0d-4d44-a175-3f6133f75db1",
    "cache-control": "no-cache",
    "origin": "https://www.birdeye.so",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.birdeye.so/",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

response = session.get(url, headers=headers, params=querystring)

with open("test.json", "w") as txt:
    txt.write(response.text)