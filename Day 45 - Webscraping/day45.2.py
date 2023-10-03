from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
#print(response.text)

soup=BeautifulSoup(response.text,"html.parser")
#links=soup.select(selector=".titleline a")
links=soup.find_all(name="span",class_="titleline")
print(len(links))
subtext_elements=soup.find_all(name="td",class_="subtext")
upvotes=[int(upvote.find(name="span",class_="score").getText().split(" ")[0]) if (upvote.find(name="span",class_="score") is not None) else 0 for upvote in subtext_elements]
print(len(upvotes))

print()
title_link_upvotes=[[]]
for i,link in enumerate(links):
    link=link.find("a")
    title_link_upvotes.append([
        link.getText(),
        link.get("href"),
        #int(upvotes[i].getText().split(" ")[0]),
        upvotes[i],
    ])

print("")
print("Articles: ")
for el in title_link_upvotes:
    if(el==[]):
        title_link_upvotes.remove(el)
        continue
    print(el[0])
    print(el[1])
    print(el[2])
    print()

print()
print("**Hottest article:** ")
largest_upvote=max(upvotes)
largest_upvote_id=upvotes.index(largest_upvote)
print(title_link_upvotes[largest_upvote_id][0])
print(title_link_upvotes[largest_upvote_id][1])
print(title_link_upvotes[largest_upvote_id][2])