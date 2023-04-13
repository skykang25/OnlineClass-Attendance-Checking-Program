#import requests #requests로 실패
from bs4 import BeautifulSoup

html=""" """  #EBS 온라인클래스 라이브 방 html 할당
soup = BeautifulSoup(html, "html.parser")
#link=soup.prettify()
temp=[]
name = soup.find_all(['span','d-inline-block px-2 white--text text-truncate text-center bottom-name-small'])
for i in name:
    temp.append(i.text)    
#print(temp)
while '' in temp:
    temp.remove('')
#print(temp[0:-11] #선생님 포함됨 주의
intact = temp[1:-11]
intact.sort() #온클방 현재 인원
# print(intact) 

namelist=[] #출석부 ['강동흔','김민우','최민수'] 식으로  

num = len(namelist)
absence = 0 #지각생 수 
late = [] #지각생이름

for a in range(0,num-1):  #출석 확인 
    if namelist[a] != intact[a-absence]:
        absence += 1
        late.append(namelist[a])

print(late)
