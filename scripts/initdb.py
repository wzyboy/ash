#!/usr/bin/env python

'''
Read tweets from Twitter archive data files and load them into an SQLite
database.
'''

import os
import glob
import json
import sqlite3
import argparse

from loader import load_files


def init_sqlite():

    ap = argparse.ArgumentParser()
    ap.add_argument('-d', '--data-dir')
    ap.add_argument('-o', '--output', default='tweets.db')
    args = ap.parse_args()

    if os.path.isfile(args.output):
        raise FileExistsError('{} already exists. Try --output, or delete it'.format(args.output))

    db = sqlite3.connect(args.output)
    cursor = db.cursor()

    if not args.data_dir:
        here = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.abspath(os.path.join(here, '../data'))
    else:
        data_dir = args.data_dir

    print('Loading tweets from data dir: {}'.format(data_dir))
    filenames = glob.glob(os.path.join(data_dir, 'js/tweets/*.js'))
    if not filenames:
        raise SystemExit('No files found. Try --data-dir')

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
