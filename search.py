from get_headers import get_header
import requests
import json
url = "https://www.ximalaya.com/revision/search/main?core=all&spellchecker=true&device=iPhone&kw=%E9%9B%AA%E4%B8%AD%E6%82%8D%E5%88%80%E8%A1%8C&page=1&rows=20&condition=relation&fq=&paidFilter=false"
s = requests.get(url,headers=get_header(),verify=False)
print(s.json())