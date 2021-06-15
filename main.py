import requests
import codecs
from bs4 import BeautifulSoup as bs

username = input('What is your trakt.tv username? ')

# Generates links based on your username
first_url = 'https://trakt.tv/users/'+ username +'/history/movies/added?genres='
base = 'https://trakt.tv/users/'+ username +'/history/movies/added?genres=&page='

# Gets the page content for the first page
results = requests.get(first_url)
src = results.content
soup = bs(src, 'lxml')

# Finds the number of pages you have
num_pages = soup.find_all(class_='page')
biggest_number = 0
for li in num_pages:
    a = li.find('a')
    number = a.get_text()
    if number != '':
        if int(number) > biggest_number:
            biggest_number = int(number)

# Writes all the movies from the first page in a .txt file
dat = codecs.open("movies.txt", "w", "utf-8")
titles = soup.find_all(class_='titles')
for title in titles:
    h3 = title.find('h3').get_text()
    dat.write(h3 + '\n')
dat.close()


i = 2
while i <= biggest_number:
    # Gets the page content for the rest of the pages
    new_url = base + str(i)
    results2 = requests.get(new_url)
    src2 = results2.content
    soup2 = bs(src2, 'lxml')

    # Writes the rest of the movies from all other pages in the same .txt file
    dat2 = codecs.open("movies.txt", "a", "utf-8")
    titles2 = soup2.find_all(class_='titles')
    for title2 in titles2:
        h3_2 = title2.find('h3').get_text()
        dat2.write(h3_2 + '\n')
    dat2.close()
    
    i += 1
