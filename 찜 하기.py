import requests, json

# 요청을 보낼 URL
url = "http://127.0.0.1:8000/zzim/20"


data = {"isLike": "False"}

response = requests.put(url, data = data)

# 응답 받기
print(response.text)
