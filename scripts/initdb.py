#!/usr/bin/env python

'''
Read tweets from Twitter archive data files and load them into an SQLite
database.
'''

import os
import json
import sqlite3
import argparse

from loader import load_data_dir


def init_sqlite():

    ap = argparse.ArgumentParser()
    ap.add_argument('-d', '--data-dir', default='data')
    ap.add_argument('-o', '--output', default='tweets.db')
    ap.add_argument('-a', '--append', action='store_true', help='insert new Tweets into existing SQLite')
    args = ap.parse_args()

    if os.path.isfile(args.output) and not args.append:
        raise FileExistsError(
            '{} already exists. Pass --output to use a different filename. '
            'If you want to insert new Tweets into existing SQLite, '
            'pass --append flag.'
            .format(args.output)
        )

    data = load_data_dir(args.data_dir)
    tweets = [
        (i['id'], i['text'], json.dumps(i))
        for i in data
    ]
    print('Loaded {} tweets'.format(len(data)))

    # Insert into SQLite
    db = sqlite3.connect(args.output)
    cursor = db.cursor()

    cursor.execute('create table if not exists tweets (id integer primary key, tweet_text text, _source text)')
    cursor.executemany('insert or ignore into tweets values (?, ?, ?)', tweets)
    print('Inserted {} tweets into SQLite'.format(cursor.rowcount))
    db.commit()

    cursor.execute('vacuum')
    db.commit()

    db.close()


if __name__ == '__main__':
    init_sqlite()
