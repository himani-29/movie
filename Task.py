# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 21:13:56 2022

@author: Himani
"""
#
#import urllib.request
#req = urllib.request.urlopen('http://www.omdbapi.com')
#print(req.read())
from bs4 import BeautifulSoup
import requests
import re


# Downloading imdb top 250 movie's data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]

crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]


ratings = [b.attrs.get('data-value')
		for b in soup.select('td.posterColumn span[name=ir]')]

id1 = [b.attrs.get('data-value')
		for b in soup.select('td.posterColumn span[name=rk]')]

votes = [b.attrs.get('data-value')
		for b in soup.select('td.ratingColumn strong')]
genres =  [b.attrs.get('data-value')
		for b in soup.select('ul.quicklinks genres')]

list = []

# create a empty list for storing
# movie information
list = []

# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
	
	# Separating movie into: 'place',
	# 'title', 'year'
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        
        genres = [a.attrs.get('href') for a in soup.select('ul.quicklinks a ')]
    
        id1=index+1
        
        movie_title = movie[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        
        data = {"movie_title": movie_title,
			"year": year,
            
			"genres": genres,
			"rating": ratings[index],
          "id1" : id1
        
			}
        list.append(data)

# printing movie details with its rating.
for movie in list:
	print( movie['movie_title'], '('+movie['year'] +
		') -', movie['rating'],movie['genres'],movie['id1'])
inid=int(input("Enter id"))
for movie in list:
 if (inid == movie['id1']):
    print( movie['movie_title'], '('+movie['year'] +
		') -', movie['rating'],movie['genres'])

inyr=int(input("Enter year"))    
for movie in list:
 if (inid == movie['id1']):
    print( movie['movie_title'], movie['rating'],movie['genres'],movie['id1'])
    
print("Print the movies details having >= 8 ratings")
rating_thresold= 8.00
for movie in list:
    if (float(movie['rating']) >= rating_thresold):
        print( movie['movie_title'], '('+movie['year'] +
		') -', movie['rating'])


    