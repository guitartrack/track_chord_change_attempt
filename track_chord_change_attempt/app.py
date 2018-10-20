from change_attempt import change_attempt

def lambda_handler(event, context):
    change_attempt(
        event['payload']['from_chord'],
        event['payload']['to_chord'],
        event['payload']['count']
    )
