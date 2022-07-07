import requests
import json

def retrieve_messages(channelid):
	headers = {
		"authorization": "token"
	}
	r = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers)
	jsonn = json.loads(r.text)
	for value in jsonn:
		author = value['author']
		username = author['username']
		print(username)

retrieve_messages("inputchannelid")