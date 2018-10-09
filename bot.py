from chat import client

if __name__=='__main__':
	question = '你好'

	answer = client.get_answer(question)
	
	print(answer)