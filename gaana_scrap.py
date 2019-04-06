import requests
from bs4 import BeautifulSoup
import pprint
import webbrowser
url = "https://gaana.com/playlist/gaana-dj-bollywood-top-50-1"
a_=requests.get(url)
soup=BeautifulSoup(a_.text,"html.parser")
main_div=soup.find("div",class_="innercontainer")
# time=main_div.find_all("li",class_="s_duration")

div = main_div.find_all("div",class_="playlist_thumb_det")
# print(div)

## scrape all hindi song according the user input##..........................##
Url_list=[]
count=1
for i in div:
	url=(i.find('a').get('href'))
	# print(url)

	Url_list.append(url)
	name = (i.find('a').text)
	print(count,name)
	count+=1
user=int(input("enter the number of song:"))
link = Url_list[user-1]
# print(link)
webbrowser.open_new_tab(link)
