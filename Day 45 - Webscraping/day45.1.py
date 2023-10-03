from bs4 import BeautifulSoup
import lxml

with open("website.html", 'r', encoding='utf-8') as file:
    contents=file.read()
    
soup=BeautifulSoup(contents,"html.parser")
#print(soup.prettify())
print(soup.title.string)
print()
all_anchor_tags=soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

print()
heading=soup.find(name="h1",id="name")
print(heading)
section_heading=soup.find(name="h3",class_="heading")
print(section_heading)
print(section_heading.get("class"))

print()
company_url=soup.select_one(selector="p a")
print(company_url)
name=soup.select_one(selector="#name")
print(name)
headings=soup.select(selector=".heading")
print(headings)