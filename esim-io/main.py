import tls_client
import random
import string
import json
import time
import re

import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_mail(email):
    # use your own logic here
    pass

def generate_account(id):
    session = tls_client.Session(client_identifier="chrome_120")
    mail = "test@gmail.com" # use your own logic here

    headers = {
        'accept': 'text/x-component',
        'accept-language': 'en-US,en;q=0.9,no;q=0.8',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://esim.io',
        'priority': 'u=1, i',
        'next-action': 'c3c483665e7c8ab6503d947b95c74ccf4960224f',
        'referer': 'https://esim.io/en/promotions/main?utm_source=facebook&utm_medium=cpc&utm_campaign=ESIM_WW_PURCHASE_FB_WEB_BAU_ALL_221124+-+yenisayfa+-+%23BLACKFRIDAY&utm_content=ESIM_WW_PURCHASE_FB_WEB_BAU_ALL_251124+-+yenisayfa+-+%23BLACKFRIDAY+-+tier1_ESIMWI155&utm_term=mix&utm_id=120214453262460425&fbclid=PAZXh0bgNhZW0BMABhZGlkAasWqfjNBukBpqRCJm990xx5QuHkj4OlMKEAbxWQn-aO6cIb-ld39fBeE7bhnBKJAwCovQ_aem_oa_L0KVtQvXzn_WE4-azbA',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'utm_source': 'facebook',
        'utm_medium': 'cpc',
        'utm_campaign': 'ESIM_WW_PURCHASE_FB_WEB_BAU_ALL_221124 - yenisayfa - #BLACKFRIDAY',
        'utm_content': 'ESIM_WW_PURCHASE_FB_WEB_BAU_ALL_251124 - yenisayfa - #BLACKFRIDAY - tier1_ESIMWI155',
        'utm_term': 'mix',
        'utm_id': '120214453262460425',
        'fbclid': 'PAZXh0bgNhZW0BMABhZGlkAasWqfjNBukBpqRCJm990xx5QuHkj4OlMKEAbxWQn-aO6cIb-ld39fBeE7bhnBKJAwCovQ_aem_oa_L0KVtQvXzn_WE4-azbA',
    }

    session.get('https://esim.io/en/promotions/main', headers=headers, params=params)
                
    data = json.dumps([mail])

    response = session.post('https://esim.io/en/promotions/main', params=params, headers=headers, data=data)
    reference_raw = response.text.split('{"reference":"')

    if len(reference_raw) != 2:
        print("No reference found (email already used recently?)")
        exit(1)

    reference_id = reference_raw[1].split('"')[0]
    print(id, "REF_ID", reference_id)

    headers["next-action"] = "55e2e8f79e82a377ae614171891e2bb8c2d289a3"
    received_mail = fetch_mail(mail)
    code = re.findall(r'(?<!#)\d{6}', received_mail["raw"])[0]
    print(id, "CODE", code)

    data = [{"reference":reference_id,"code":code,"campaignId":"SMESIMAPP"}]
    data = json.dumps(data, separators=(',', ':'))

    # print(id, "SUBMITTING CODE")

    response = session.post('https://esim.io/en/promotions/main', params=params, headers=headers, data=data)

    # print(id, "SUBMITTED CODE... WAITING FOR EMAIL")
    received_mail = fetch_mail(mail)
    
    if received_mail is None:
        print(id, "NO EMAIL RECEIVED, FAILED")
        return
    else:
        print(id, "EMAIL RECEIVED, ACCOUNT SUCCESSFULLY CREATED\n")
        
        with open("accounts.txt", "a") as f:
            f.write(f"{mail}\n")

if __name__ == "__main__":
    max_workers = 150
    accounts_to_generate = 1000

    print(f"Generating {accounts_to_generate} accounts with {max_workers} workers")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i in range(accounts_to_generate):
            executor.submit(generate_account, f"TASK #{i + 1}")
