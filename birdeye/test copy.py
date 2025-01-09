import tls_client
import uuid

session = tls_client.Session(client_identifier="chrome_116")

url = "https://multichain-api.birdeye.so/solana/trending/token"

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,no;q=0.8',
    'agent-id': str(uuid.uuid4()),
    'cache-control': 'no-cache',
    'origin': 'https://www.birdeye.so',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.birdeye.so/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

response = session.get(url, headers=headers)

with open("test.json", "w") as txt:
    txt.write(response.text)