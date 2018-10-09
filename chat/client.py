import requests

def get_answer(text):
	url = 'https://api.ownthink.com/bot?info=%s'%text
	sess = requests.get(url)

	text = sess.text
	
	text = eval(text)
	
	
	return text
