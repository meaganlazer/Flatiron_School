top_500=[]
import csv
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        from collections import OrderedDict
        top_500.append(dict(row))
top_500

text_file = open('top-500-songs.txt', 'r')
lines = text_file.readlines()
updated_lines= []
dict_list = []
for i in range(len(lines)):
    updated_lines.append(lines[i].split("\t"))
for item in updated_lines:
    dict_list.append{'rank':item[0], 'name': item[1], 'artist':item[2]'year':item[3]}
print(dict_list)


def album_name():
album = "Back to Mono"

def find_by_name(album_name):
    album_dict = None
    for item in top_500:
        if item ['album'] == album_name:
            album_dict = item
    return album_dict

find_by_name(album)


    
number = "19"

def find_by_number(album_number):
    album_dict = None
    for item in top_500:
        if item ['number'] == album_number:
            album_dict = item
    return album_dict

find_by_number(number)    


    
year = "1965"

def find_by_year(album_year):
    album_dict = None
    for item in top_500:
        if item ['year'] == album_year:
            album_dict = item
    return album_dict

find_by_year(str(year))

def album_rank

def album_year

def start_years end years

def start_end_ranks

def album_titles

def artist_name

def artists most albums

def most popular word album title

def histogram of albums by decade
import matplotlib.pyplot as plt

def histogram by genre

albumWithMostTopSongs - returns the name of the artist and album that has that most songs featured on the top 500 songs list

albumsWithTopSongs - returns a list with the name of only the albums that have tracks featured on the list of top 500 songs

songsThatAreOnTopAlbums - returns a list with the name of only the songs featured on the list of top albums

top10AlbumsByTopSongs - returns a histogram with the 10 albums that have the most songs that appear in the top songs list. The album names should point to the number of songs that appear on the top 500 songs list.

topOverallArtist - Artist featured with the most songs and albums on the two lists. This means that if Brittany Spears had 3 of her albums featured on the top albums listed and 10 of her songs featured on the top songs, she would have a total of 13. The artist with the highest aggregate score would be the top overall artist.