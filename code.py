import re
import requests

url='http://csszengarden.com/'
res=requests.get(url)

page_content=res.text

regex=re.compile('class="design-name">(.*?)</a> by')

result=regex.findall(page_content)

print("Design Name:")
for i in result:
    print(i)
