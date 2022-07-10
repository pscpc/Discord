import threading
import requests
import time
import random


channel = "inputchannelid"
mess = ["input mess text"]
delay = 0.1
with open("tokens.txt", "r") as file:
    allText = file.read()
    tokens = list(map(str, allText.split()))
    random.shuffle(tokens)

def spam(token, channel, mess):
    url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
    data = {"content": mess}
    header = {"authorization": token}
    r = requests.post(url, data=data, headers=header)



def thread():
    channel_id = channel
    text=mess
    for token in tokens:
        random.shuffle(mess)
        random.shuffle(tokens)
        time.sleep(delay)
        threading.Thread(target=spam, args=(token, channel_id, text)).start()

thread()