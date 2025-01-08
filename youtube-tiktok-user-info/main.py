import requests

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,no;q=0.8',
    'authorization': '',
    'cache-control': 'no-cache',
    'origin': 'https://www.tiktokviewcount.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.tiktokviewcount.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

params = {
    'username': 'sinchisan',
    'service': 'SHORTS',
}

proxy = "..."
proxies = {
    "http": proxy,
    "https": proxy,
}

response = requests.get('https://api.buzzlytics.io/metadata', params=params, headers=headers, proxies=proxies)

response = requests.get('https://api.buzzlytics.io/jobs', params=params, headers=headers)
