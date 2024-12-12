from bs4 import BeautifulSoup
from icecream import ic
import requests

with open('index.html', 'r') as file:
    doc = BeautifulSoup(file, 'html.parser')
    
    ic(doc)
tag = doc.title
ic(tag)
tag.string = 'New Title'
ic(tag)
ptag = doc.find_all('p')
ic(ptag)

url = "https://www.newegg.com"

result = requests.get(url)
ic(result.text)
doc = BeautifulSoup(result.text, 'html.parser')
ic(doc)
prices = doc.find_all(text='$')
#