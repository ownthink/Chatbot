from chat import server

if __name__=='__main__':
	question = '你好'

	answer = server.get_answer(question)
	
	print(answer)