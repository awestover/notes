
import requests 
import json
import random

"""
https://www.datamuse.com/api/
https://www.rhymezone.com/

this is a very fun website, useful if you are writing a poem
"""


def getURL(ml, rel_rhy):
	return "https://api.datamuse.com/words?ml={}&rel_rhy={}".format(ml, rel_rhy)

sent = "Bob are three brown mice"
with open("test.txt", 'r') as f:
	sent = f.read()
new_sent = ""

for w in sent.split():
	data = requests.get(getURL(w,w))
	dataJson = json.loads(data.content)
	print(dataJson)
	if len(dataJson) > 0:
		new_sent += dataJson[0]['word']
	else:
		new_sent += w
	new_sent += " "

with open("out.txt", 'w') as f:
	f.write(new_sent)
