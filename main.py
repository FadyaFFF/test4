from bs4 import BeautifulSoup
import requests
        
with open('C:/Parsing/index.html', encoding='utf-8') as file:
    src = file.read()

# print(src)    
soup = BeautifulSoup(src, 'lxml')

# main_h1 = soup.find('h1', class_='mainH1')
# print(main_h1.string.strip())

parents = soup.find_parent('ulFirst').find_parents('ulFirst').text()
print(parents)