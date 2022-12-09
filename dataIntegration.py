import csv
from difflib import SequenceMatcher
from enum import Enum

DATASETS_FILEPATH = 'Datasets'
MINIMUM_MATCH_PERCENTAGE = 0.8
NUMBER_OF_ITERATIONS = 5000

class Entries(Enum):
    NAME = 1
    ALBUM = 2
    ARTIST = 4
    DANCEABILITY = 9    
    ENERGY = 10
    KEY = 11
    ACOUSTICNESS = 15
    INSTRUMENTALNESS = 16
    VELANCE = 18
    TEMPO = 19
    DURATION = 20
    YEAR = 22

songs = {}

f = open('integratedData.csv', 'w')
writer = csv.writer(f)

# guitarTabs header: Artist,Song Name,Song Rating,Song Hits,Page Type,Difficulty,Key,Capo,Tuning
with open(DATASETS_FILEPATH + '/gutiarTabs.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True
    songId = 0
    for row in csv_reader:
        if not first:
            songName = row[1].strip()
            songs[songName] = []
            songs[songName].append(songId)
            songs[songName].append(songName)
            songs[songName].append(row[0])
            songs[songName].append(row[5])
            songs[songName].append(row[6])
            songs[songName].append(row[7])
            songs[songName].append(row[8])
            songId += 1
        else:
            first = False

"""id,name,album,album_id,artists,
artist_ids,track_number,disc_number,
explicit,danceability,energy,key,loudness,
mode,speechiness,acousticness,instrumentalness,
liveness,valence,tempo,duration_ms,time_signature,
year,release_date"""

with open(DATASETS_FILEPATH + '/tracks_features.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True
    rows = list(csv_reader)
    for song in songs:
        iterator = 1
        songFound = False
        while not songFound and iterator < NUMBER_OF_ITERATIONS:
            row = rows[iterator]
            songMatchPercentage = SequenceMatcher(a=song, b=row[1]).ratio()
            if songMatchPercentage > MINIMUM_MATCH_PERCENTAGE:
                songsArtistName = songs[song][2]
                csvArtistName = row[4].split("'")[1]
                songArtistMatchPercentage = SequenceMatcher(a=songsArtistName, b=csvArtistName).ratio()
                if songArtistMatchPercentage > MINIMUM_MATCH_PERCENTAGE:
                    songs[song].append(row[Entries.ALBUM.value].strip())
                    songs[song].append(row[Entries.DANCEABILITY.value])
                    songs[song].append(row[Entries.ENERGY.value])
                    songs[song].append(row[Entries.KEY.value])
                    songs[song].append(row[Entries.ACOUSTICNESS.value])
                    songs[song].append(row[Entries.INSTRUMENTALNESS.value])
                    songs[song].append(row[Entries.VELANCE.value])
                    songs[song].append(row[Entries.TEMPO.value])
                    songs[song].append(row[Entries.DURATION.value])
                    songs[song].append(row[Entries.YEAR.value])
                    songs[song].append("No Lyrics")
                    songFound = True
            iterator += 1
        if iterator >= NUMBER_OF_ITERATIONS:
            songs[song].append("No Album info")
            songs[song].append(0.0)
            songs[song].append(0.0)
            songs[song].append(0.0)
            songs[song].append(0.0)
            songs[song].append(0.0)
            songs[song].append(0.0)
            songs[song].append(0.0)
            songs[song].append("No Duration info")
            songs[song].append("No Year info")
            songs[song].append("No Lyrics info")

# lyrics header: id,artist,seq,song,label
with open(DATASETS_FILEPATH + '/lyrics.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True
    songId = 0
    rows = list(csv_reader)
    for song in songs:
        iterator = 1
        songFound = False
        while not songFound and iterator < NUMBER_OF_ITERATIONS:
            row = rows[iterator]
            songMatchPercentage = SequenceMatcher(a=song, b=row[3]).ratio()
            if songMatchPercentage > MINIMUM_MATCH_PERCENTAGE:
                songsArtistName = songs[song][2]
                csvArtistName = row[1]
                songArtistMatchPercentage = SequenceMatcher(a=songsArtistName, b=csvArtistName).ratio()
                if songArtistMatchPercentage > MINIMUM_MATCH_PERCENTAGE:
                    songs[song][17] = row[2]
                    songFound = True
            iterator += 1

# Final format: 
# id, songName, artistName, difficulty, tone, capo, tuning, album, danceability, energy, key, acousticness, intrumentalness, velance, tempo, duration, year, lyrics
for song in songs:
    writer.writerow(songs[song])

f.close()