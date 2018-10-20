from model import ChordChangeAttempt

def change_attempt(from_chord: str, to_chord: str, count: int):
    attempt = ChordChangeAttempt(
        chord_change='{}:{}'.format(from_chord, to_chord), count=count)
    attempt.save()
