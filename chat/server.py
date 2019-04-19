import json
import requests

def get_answer(text):
	url = 'https://api.ownthink.com/bot?spoken=%s'%text
	sess = requests.get(url)

	text = sess.text
	
	text = json.loads(text)

	
	return text
