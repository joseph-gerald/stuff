from bs4 import BeautifulSoup
import requests

my_ip = requests.get("https://checkip.amazonaws.com").text.strip()

def ip_check(proxy, retry=0):
    proxy_ip = "no ip"

    try:
        response = requests.get("https://checkip.amazonaws.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        proxy_ip = response.text.strip()

        if proxy_ip != my_ip:
            return (proxy_ip, True)
    except:
        if retry < 3:
            return ip_check(proxy, retry + 1)
        pass

    return (proxy_ip, False)

def get_fraud_score(proxy, retry=0):
    proxy_ip = "no ip"

    try:
        response = requests.get("https://checkip.amazonaws.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        proxy_ip = response.text.strip()

        if proxy_ip != my_ip:
            response = requests.get("https://scamalytics.com/ip/" + response.text.strip(), timeout=5)
            soup = BeautifulSoup(response.text, "lxml")

            fraud_score = soup.find("div", class_="score").text
            
            return (proxy_ip, int(fraud_score.split("Fraud Score: ")[1]))
    except:
        if retry < 3:
            return get_fraud_score(proxy, retry + 1)
        pass

    return (proxy_ip, -1)

def resi_check(proxy, retry=0):
    proxy_ip = "no ip"

    try:
        response = requests.get("https://checkip.amazonaws.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        proxy_ip = response.text.strip()

        if proxy_ip != my_ip:
            response = requests.get("https://api.jooo.tech/ipr", proxies={"http": proxy, "https": proxy}, timeout=5)
            data = response.json()

            return (proxy_ip, data["residential"])
    except:
        if retry < 3:
            return resi_check(proxy, retry + 1)
        pass

    return (proxy_ip, False)

if __name__ == "__main__":
    print(get_fraud_score(""))