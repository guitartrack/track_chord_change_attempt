from datetime import datetime

from pynamodb.models import Model
from pynamodb.attributes import (
    NumberAttribute, UnicodeAttribute, UTCDateTimeAttribute)


class ChordChangeAttempt(Model):
    class Meta:
        table_name = "chord_change_attempt"
        region = 'eu-central-1'

    chord_change = UnicodeAttribute(hash_key=True)
    created_at = UTCDateTimeAttribute(default=datetime.utcnow, range_key=True)

    count = NumberAttribute()


def lambda_handler(event, context):
    change_attempt(
        event['payload']['from_chord'],
        event['payload']['to_chord'],
        event['payload']['count']
    )


def change_attempt(from_chord: str, to_chord: str, count: int):
    attempt = ChordChangeAttempt(
        chord_change='{}:{}'.format(from_chord, to_chord), count=count)
    attempt.save()
