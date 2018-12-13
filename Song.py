import requests
from bs4 import BeautifulSoup
import os

#specify the url
Artist_name =input("Artist Name or Movie Name :").replace(' ','+')
stype ="5570"
domain_name ="https://www.pagalworld.io"
wiki = "https://www.pagalworld.io/search?cats="+stype+"&q="+Artist_name+"&page="
page = 1

Link_list =[]
song_name =[]
prv =[]
while True:
    cur =[]
    source = requests.get(wiki+str(page)).text
    page+=1
    soup = BeautifulSoup(source,"lxml")
    link_data =soup.find_all('div', class_='listbox')
    if len(link_data)>0:
        for href in link_data:
            cell = href.find('a')
            if cell.text.strip() not in song_name:
                Link_list.append(cell['href'])
                song_name.append(cell.text.strip())
                cur.append(cell.text.strip())
    else:
        print("No record found !!!")
    if cur == prv:
        break
    prv = cur

print(Artist_name,"Songs :-")
count=0
for song in song_name:
    print("\t\t",count,song)
    count+=1
song_num = list(map(int,input("Enter song Numbers(sepersted by ','):").split(",")))
n=0    
for i in song_num:
    os.system('clear')
    n+=1
    response=requests.get(domain_name+Link_list[i]).text
    soup1 = BeautifulSoup(response,"lxml")
    result= soup1.find('a',class_='dbutton')
    downlink= result['href']
    songname=result['title']
    print("[ Downloding ",n,"-",len(song_num),"]")
    print(result['title'])
    drspn = requests.get(downlink)
    file = open(songname[9:],'wb')
    file.write(drspn.content)
    