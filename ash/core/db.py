from ast import literal_eval
from collections.abc import Mapping

from ash.models import Tweet


class TweetsDatabase(Mapping):

    def __init__(self):
        self.model = Tweet

    def __getitem__(self, tweet_id):
        if not isinstance(tweet_id, int):
            raise TypeError('Tweet ID should be int')
        try:
            return self.model.objects.get(pk=tweet_id)
        except self.model.DoesNotExist:
            return None

    def __iter__(self):
        for i in self.model.objects.values_list('id', flat=True):
            yield i

    def __reversed__(self):
        for i in self.model.objects.values_list('-id', flat=True):
            yield i

    def __len__(self):
        return self.model.objects.all().count()

    @staticmethod
    def _row_to_tweet(row):
        return literal_eval(row._raw)

    def search(self, keyword=None, user_screen_name=None, limit=100):
        q = self.model.objects.all()
        if keyword:
            q = q.filter(text__contains=keyword)
        if user_screen_name:
            q = q.filter(user_screen_name=user_screen_name)
        q = q[:limit]

        tweets = [self._row_to_tweet(row) for row in q]
        return tweets
