import csv
import numpy as np

DATASETS_FILEPATH = 'Datasets'

songsIds = []

with open(DATASETS_FILEPATH + '/tracks_features.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count > 0 and line_count <= 2664:
            songsIds.append(line_count)
        line_count += 1

# open the file in the write mode
f = open('integratedData.csv', 'w')
writer = csv.writer(f)
writer.writerow(songsIds)
f.close()
