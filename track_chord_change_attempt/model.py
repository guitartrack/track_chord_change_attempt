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
