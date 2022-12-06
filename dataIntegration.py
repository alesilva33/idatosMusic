import csv
from difflib import SequenceMatcher
import numpy as np

from enum import Enum

DATASETS_FILEPATH = 'Datasets'
MINIMUM_MATCH_PERCENTAGE = 0.8

class Entries(Enum):
    NAME = 1
    ALBUM = 2
    ALBUM_ID = 3
    ARTIST = 4
    ARTIST_ID = 5
    DANCEABILITY = 9
    ENERGY = 10
    KEY = 11
    ACOUSTICNESS = 15
    INSTRUMENTALNESS = 16
    VELANCE = 18
    TEMPO = 19
    DURATION = 20
    YEAR = 22

"""id,name1,album2,album_id3,artists4,artist_ids5,
track_number6,disc_number7,explicit8,danceability9,
energy10,key11,loudness12,mode13,speechiness14,acousticness15,
instrumentalness16,liveness17,valence18,tempo19,duration_ms20,
time_signature21,year22,release_date23"""

songs = {}
songsIds = []
songsNames = []
songsAlbums = []
albumsIds = []
artists = []
artistsIds = []
trackNumbers = []
disc_number = []
danceability = []
energy = []
key = []
loduness = []
acousticness = []
tempos = []
durations = []
years = []

f = open('integratedData.csv', 'w')
writer = csv.writer(f)
with open(DATASETS_FILEPATH + '/tracks_features.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True
    songId = 0
    for row in csv_reader:
        if not first:
            songName = row[Entries.NAME.value].strip()
            songs[songName] = []
            songs[songName].append(songId)
            songs[songName].append(songName)
            songs[songName].append(row[Entries.ALBUM.value].strip())
            songs[songName].append(row[Entries.ALBUM_ID.value])
            songs[songName].append(row[Entries.ARTIST.value][0])
            songs[songName].append(row[Entries.ARTIST_ID.value][0])
            songs[songName].append(row[Entries.DANCEABILITY.value])
            songs[songName].append(row[Entries.ENERGY.value])
            songs[songName].append(row[Entries.KEY.value])
            songs[songName].append(row[Entries.ACOUSTICNESS.value])
            songs[songName].append(row[Entries.TEMPO.value])
            songs[songName].append(row[Entries.DURATION.value])
            songs[songName].append(row[Entries.YEAR.value])
            #writer.writerow(songs[songName])
            """ songs[songId] = []
            songs[songId].append(songId)
            songs[songId].append(row[Entries.NAME.value].strip())
            songs[songId].append(row[Entries.ALBUM.value].strip())
            songs[songId].append(row[Entries.ALBUM_ID.value])
            songs[songId].append(row[Entries.ARTIST.value][0])
            songs[songId].append(row[Entries.ARTIST_ID.value][0])
            songs[songId].append(row[Entries.DANCEABILITY.value])
            songs[songId].append(row[Entries.ENERGY.value])
            songs[songId].append(row[Entries.KEY.value])
            songs[songId].append(row[Entries.ACOUSTICNESS.value])
            songs[songId].append(row[Entries.TEMPO.value])
            songs[songId].append(row[Entries.DURATION.value])
            songs[songId].append(row[Entries.YEAR.value])
            writer.writerow(songs[songId]) """
            songId += 1
        else:
            first = False

with open(DATASETS_FILEPATH + '/lyrics.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True
    songId = 0
    for row in csv_reader:
        if not first:
            # Formato row: id,artist,seq,song,label
            songArtist = row[1]
            songLyrics = row[2]
            songName = row[3]
            songFound = False
            songIterator = 0
            while not songFound:
                songsSongName = songs.keys()[songIterator]
                songMatchPercentage = SequenceMatcher(songsSongName=songsSongName, songName=songName).ratio()
                if songMatchPercentage > MINIMUM_MATCH_PERCENTAGE:
                    songsArtistName = songs[songsSongName][5]
                    songArtistMatchPercentage = SequenceMatcher(songsArtistName=songsArtistName, songArtist=songArtist).ratio()
                    if songArtistMatchPercentage > MINIMUM_MATCH_PERCENTAGE:
                        songs[songsSongName].append(songLyrics)
        else:
            first = False
f.close()

# open the file in the write mode
"""f = open('integratedData.csv', 'w')
writer = csv.writer(f)
writer.writerow(songs)
f.close()"""