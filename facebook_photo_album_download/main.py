import requests
import json

images = json.loads(open("images.json","r").read())

for image_url in images:
    response = requests.get(image_url)

    file_name = image_url.split("/")[-1].split("?")[0]

    with open("images/"+file_name, "wb") as file:
        file.write(response.content)
        print ("Downloaded: "+file_name)