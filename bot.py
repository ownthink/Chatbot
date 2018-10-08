import requests

url = 'https://api.ownthink.com/bot?info=你好'      # 口语理解API
sess = requests.get(url) # 请求

text = sess.text # 获取返回的数据
print(text) 

text = eval(text) # 转为字典类型
print(text)
