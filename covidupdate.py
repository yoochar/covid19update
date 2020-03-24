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

print("**********************************")

url="https://covid19.workpointnews.com/api/_constants"
resp=requests.get(url)

data=resp.json()
stat=[]
for item in data:
    print(item + ":" + data[item])
    stat.append(data[item])





url = "https://notify-api.line.me/api/notify"
sentMsg = "message=" + "Total:" + stat[5] + ",Recover:" + stat[1]

x = requests.post(url, data = sentMsg ,  headers = {"content-type": "application/x-www-form-urlencoded","Authorization": "Bearer 9W6q1qMdR8kPHx09LHJo1MkB77VrkO6A0EiVohwhQLX"})

print(x.text)

