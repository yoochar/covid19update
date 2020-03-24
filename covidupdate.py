import requests
from bs4 import BeautifulSoup

url="https://ddc.moph.go.th/viralpneumonia/"
data=requests.get(url)
#print(data.status_code)
#print(data.text)

soup=BeautifulSoup(data.text,'html.parser')

result =soup.find_all("td",{"class":"popup_num txt"})
for item in result:
    print(item)