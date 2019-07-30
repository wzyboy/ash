from django.db import models


class Tweet(models.Model):

    id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    user_id = models.IntegerField()
    user_screen_name = models.CharField(max_length=32)
    text = models.TextField()

    class Meta:
        db_table = 'tweets'

    def __repr__(self):
        return f'<Tweet {self.id}>'
