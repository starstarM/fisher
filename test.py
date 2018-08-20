import requests


url = 'http://t.yushu.im/v2/book/isbn/9787807591481'

request = requests.get(url)

print(request.json())
print(request.status_code)