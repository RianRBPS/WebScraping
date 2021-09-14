import requests
import bs4

result = requests.get('http://www.example.com')

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

soup = bs4.BeautifulSoup(res.text,'lxml')
# soup

first_item = soup.select('.toctext')[0]

first_item.text

for item in soup.select('.toctext'):
    print(item.text)

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

soup = bs4.BeautifulSoup(res.text,'lxml')

soup.select('.thumbimage')

computer = soup.select('.thumbimage')[0]

computer['src']


src = '//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png'