import os
import csv
import collections
from typing import List

data = []

Record = collections.namedtuple(
    'Record',
    'server,seconds_before_next_point,'
    'day,opponent,game_score,set,game'
)

def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', "serve_times.csv")

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)

def parse_row(row):
    row['server'] = str(row['server'])
    row['seconds_before_next_point'] = int(row['seconds_before_next_point'])
    # row['day'] = datetime(row['day'])
    row['opponent'] = str(row['opponent'])

    # game_score, set, game

    record = Record(
        **row
    )

    return record

def fastest_servers()  -> int:
    return sorted(data)
