import requests

result = requests.get("http://www.example.com")
type(result)

result.text

###################################################

import bs4
soup = bs4.BeautifulSoup(result.text,'lxml') # lxml backend of bs4
print(soup)

###################################################

soup.select('title')[0].getText()

site_paragraphs = soup.select('p') # paragraph

soup.select('h1')

site_paragraphs[0].getText() #bs4.element.Tag

# Learn more about HTML Tags 