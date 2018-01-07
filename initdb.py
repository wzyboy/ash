#!/usr/bin/env python

import os
import glob
import json
import sqlite3

from loader import load_files


def init_sqlite():

    db = sqlite3.connect('tweets.db')
    cursor = db.cursor()

    here = os.path.dirname(os.path.abspath(__file__))
    filenames = glob.glob(os.path.join(here, 'data/js/tweets/*.js'))
    data = load_files(filenames)
    tweets = [
        (i['id'], i['text'], json.dumps(i))
        for i in data
    ]
    print('Loaded {} tweets'.format(len(data)))

    cursor.execute('create table tweets (id integer primary key, tweet_text text, _source text)')
    cursor.executemany('insert into tweets values (?, ?, ?)', tweets)
    db.commit()

    cursor.execute('vacuum')
    db.commit()

    db.close()


if __name__ == '__main__':
    init_sqlite()
