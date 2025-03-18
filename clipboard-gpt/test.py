import json
import requests
import pyperclip
from openai import OpenAI
import os

# check if convo.json exists

SYSTEM_PROMPT = "You are a helpful assistant."
CONVERSATION = []

if not os.path.exists("convo.json"):
    with open("convo.json", "w") as f:
        json.dump([
            {"role": "system", "content": SYSTEM_PROMPT },
        ], f)

with open("convo.json", "r") as f:
    CONVERSATION = json.load(f)

clipboard_content = pyperclip.paste()

CONVERSATION.append({"role": "user", "content": clipboard_content})

pyperclip.copy("PLEASE_WAIT")

client = OpenAI(
    api_key="",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=CONVERSATION,
)

chat_message = completion.choices[0].message.content

CONVERSATION.append({ "role": "assistant", "content": chat_message })

with open("convo.json", "w") as f:
    json.dump(CONVERSATION, f)

pyperclip.copy(chat_message)