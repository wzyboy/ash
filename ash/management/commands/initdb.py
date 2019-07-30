'''
Read tweets from Twitter archive data files and load them into an SQLite
database.
'''

from datetime import datetime

from django.core.management import BaseCommand

from ash.core.loader import load_data_dir
from ash.models import Tweet


def parse_datetime(s):
    # 2017-10-09 04:39:56 +0000
    return datetime.strptime(s, '%Y-%m-%d %H:%M:%S %z')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-d', '--data-dir', default='data')

    def handle(self, *args, **kwargs):

        data = load_data_dir(kwargs['data_dir'])
        tweets = [
            Tweet(
                id=i['id'],
                created_at=parse_datetime(i['created_at']),
                user_id=i['user']['id'],
                user_screen_name=i['user']['screen_name'],
                text=i['text'],
            )
            for i in data
        ]
        Tweet.objects.bulk_create(tweets)
