def lambda_handler(event, context):

    from os import environ
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    from random import choice

    client = WebClient(token=environ['SLACK_TOKEN'])
    duty_member_list = environ['MEMBERS'].split(',')

    try:
        response = client.chat_postMessage(
            channel=environ['SLACK_CHANNEL'],
            text=f"오늘의 청소당번은 {choice(duty_member_list)}님 입니다."
        )
        print(response)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'

    return 0