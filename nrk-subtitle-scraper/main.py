import requests

for i in range(300):
    number_to_pad = i
    padded_number = str(number_to_pad).zfill(4)

    url = f"https://nrk-od-world-39.akamaized.net/open/ps/nnfa/nnfa56022723/0957595d-5.smil/sc-gaFEQg/s0_F{number_to_pad}.webvtt"
    res = requests.get(url)

    with open("subtitles.txt", "a", encoding="utf-8") as f:
        f.write("\n".join(res.text.split("\n")[:-3]))
