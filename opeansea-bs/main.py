from curl_cffi import requests
from concurrent.futures import ThreadPoolExecutor
import json
import bs4

import random

proxies = open("proxies.txt", "r").read().split("\n")

def get_proxy():
    return random.choice(proxies)

class CryptoPunk:
    def __init__(self, id, address, magic_eden_or_ens, numbers_owned, last_active):
        self.id = id
        self.address = address
        self.magic_eden_or_ens = magic_eden_or_ens
        self.numbers_owned = numbers_owned
        self.last_active = last_active

    def __str__(self):
        return f"{self.id} {self.address} {self.magic_eden_or_ens} {self.numbers_owned} {self.last_active}"

class OpenSeaAccount:
    def __init__(self, address, display_name, bio, image_url, twitter):
        self.address = address
        self.display_name = display_name
        self.bio = bio
        self.image_url = image_url
        self.twitter = twitter

    def __str__(self):
        return f"{self.address},{self.display_name},{self.bio},{self.image_url},{self.twitter}"

def get_leaderboard():
    res = requests.get("https://cryptopunks.app/cryptopunks/leaderboard")

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    table = soup.find("table")

    owners = []

    for row in table.find_all("tr"):
        cols = row.find_all("td")

        if len(cols) > 1:
            rank = cols[0].text.strip()
            address = cols[1].find("a")["href"].replace("/cryptopunks/accountinfo?account=", "") if cols[1].find("a") else None
            magic_eden_or_ens = cols[2].find("a")["href"] if cols[2].find("a") else None
            numbers_owned = cols[3].text.strip() if cols[3].text.strip() else None
            last_active = cols[4].text.strip() if cols[4].text.strip() else None

            owners.append(CryptoPunk(rank, address, magic_eden_or_ens, numbers_owned, last_active))

    return owners

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,no;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def lookup_opensea(address):
    try:
        proxy = get_proxy()

        res = requests.get("https://opensea.io/" + address, headers=headers, proxies={
            "http": proxy,
            "https": proxy
        }, timeout=20)

        # if res.status_code != 200: retry

        if res.status_code != 200:
            print(f"Failed to fetch {address}")
            return lookup_opensea(address)

        # print(res.text)

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        # get __NEXT_DATA__ element from page (BY ID)
        #print(res.text)
        data = soup.find("script", {"id": "__NEXT_DATA__"}).string

        # parse JSON from __NEXT_DATA__ element

        json_data = json.loads(data)

        with open("data.json", "w") as f:
            f.write(json.dumps(json_data, indent=4))

        initial_records = json_data["props"]["pageProps"]["initialRecords"]

        index = 0
        account = None

        for record in initial_records:
            index += 1
            if (index == 2):
                # print(initial_records[record])

                info = initial_records[record]

                address = info["address"]
                display_name = info["displayName"]
                bio = info["bio"]
                image_url = info["imageUrl"]
                twitter = info["connectedTwitterUsername"]

                account = OpenSeaAccount(address, display_name, bio, image_url, twitter)

        return account
    except Exception as e:
        print(f"ERROR ! Failed to fetch {address}")
        return lookup_opensea(address)

def lookup_opensea_and_save(address):
    print(f"Looking up {address}")
    account = lookup_opensea(address)
    print(f"Found {account}")

    with open("opensea_accounts.txt", "a", encoding="utf-8") as f:
        f.write(str(account) + "\n")

def find_account_type(obj):
    if "__typename" in obj and obj["__typename"] == "AccountType":
        return obj
    else:
        for key in obj:
            if type(obj[key]) == dict:
                res = find_account_type(obj[key])
                if res:
                    return res
                

def lookup_punk(index):
    try:
        proxy = get_proxy()
        res = requests.get(f"https://opensea.io/assets/ethereum/0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb/{index}", proxies={
            "http": proxy,
            "https": proxy
        }, headers=headers, timeout=20)

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        # print(res.text)

        data = soup.find("script", {"id": "__NEXT_DATA__"}).string

        json_data = json.loads(data)

        with open("data.json", "w") as f:
            f.write(json.dumps(json_data, indent=4))

        # iterate through all children until object with __typename == "AccountType" is found

        account_type = find_account_type(json_data)

        return account_type["address"]
    except Exception as e:
        print(e)
        print(f"Failed to fetch punk {index}")
        return lookup_punk(index)

def lookup_store_punk(index):
    print(f"Looking up punk {index}")
    owner = lookup_punk(index)
    print(f"Found owner {owner}")
    with open("punks.txt", "a") as f:
        f.write(f"{index},{owner}\n")

def check_username_availability(username):
    try:
        proxy = get_proxy()
        res = requests.post(f"https://checkuser.org/twitter-availability-checker/availability_checker.php", data={
            "username": username
        }, proxies={
            "http": proxy,
            "https": proxy
        }, headers={
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9,no;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://checkuser.org',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://checkuser.org/twitter-availability-checker/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }, timeout=20)

        return res.json()["social_media"]["twitter.com"]
    except Exception as e:
        print(f"Failed to fetch {username}")
        return check_username_availability(username)

if __name__ == "__main__":
    print(check_username_availability("ATS_Crypto1232"))

    exit()
    with ThreadPoolExecutor(max_workers=500) as executor:
        for i in range(500, 10_000):
            executor.submit(lookup_store_punk, i)
        

    exit()
    print(lookup_opensea("ATS_Crypto"))
    exit()
    leaderboard = get_leaderboard()

    open("punk_owners.txt", "w").close()

    with open("punk_owners.txt", "a", encoding="utf-8") as f:
        for punk in leaderboard:
            f.write(str(punk).replace("\n", "_NEW_LINE_") + "\n")

    max_workers = 50

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for punk in leaderboard:
            executor.submit(lookup_opensea_and_save, punk.address)
