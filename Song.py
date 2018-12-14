#Script to Download Songs all songs (By artist or By Movie name)
#This script only works on WWW.pagalworal.io

#Modules to sent request to server
import requests
#Module to handel the content of site 
from bs4 import BeautifulSoup
import os

#Input [artist name or movie name]
Artist_name =input("Artist Name or Movie Name :").replace(' ','+')

#Domain form are we are downloading song
domain_name ="https://www.pagalworld.io"
URL = "https://www.pagalworld.io/search?cats=5570&q="+Artist_name+"&page="
page = 1

song_links =[]	#Links of songs
song_names =[]	#Song names
prv =[]
while True:
    cur =[]
    #sending request to server and storing site content to source
    source = requests.get(URL+str(page)).text
    page+=1
    #Beautifulsoup is useto handle site content [HTML,CSS,etc souce code of site]
    soup = BeautifulSoup(source,"lxml")

    #Fnding all division tag [because all the links of songes are in Div tag]
    div_tag_data =soup.find_all('div', class_='listbox')

    #Finding all the link and song name from all div tag and storing in list
    if len(div_tag_data)>0:
        for href in div_tag_data:
            cell = href.find('a')
            if cell.text.strip() not in song_name:
                song_links.append(cell['href'])
                song_names.append(cell.text.strip())
                cur.append(cell.text.strip())
    else:
        print("No record found !!!")
    if cur == prv:
        break
    prv = cur

print(Artist_name,"Songs :-")
count=0

#Display all song according to search result
for song in song_names:
    print("\t\t",count,song)
    count+=1

#Input to select song to download
song_num = list(map(int,input("Enter song Numbers(sepersted by ','):").split(",")))

#Code to download song
n=0    
for i in song_num:
    os.system('clear')
    n+=1
    response=requests.get(domain_name+song_links[i]).text
    soup1 = BeautifulSoup(response,"lxml")
    result= soup1.find('a',class_='dbutton')
    downlink= result['href']
    songname=result['title']
    print("[ Downloding ",n,"-",len(song_num),"]")
    print(songname[9:])
    download_song = requests.get(downlink)
    file = open(songname[9:],'wb')
    file.write(download_song.content)
    
