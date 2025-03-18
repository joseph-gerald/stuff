import json
import requests
import pyperclip


clipboard_content = pyperclip.paste()

pyperclip.copy("PLEASE_WAIT")

params = {
    "model": "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
    "q": clipboard_content,
    "c": "You are a intelligent ai model which will try to answer questions quickly and accurately whilst not wasting time on unnecessary details unless instructed to.",
    #"c": "You are a MATH solver robot, all you do is get math questions and ONLY provide the answers and not any comments or explanations.",
}

r = requests.get("https://mistral.jooo.tech", params=params)

response = r.json()["response"]
print(response)
pyperclip.copy(response)