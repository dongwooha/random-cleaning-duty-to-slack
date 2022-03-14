import random

def lambda_handler(event, context):

    from os import environ
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    from random import choice
    from random import sample


    client = WebClient(token=environ['SLACK_TOKEN'])
    duty_member_list = environ['MEMBERS'].split(',')

    try:
        response = client.chat_postMessage(
            channel=environ['SLACK_CHANNEL'],
            text=f"이번주 밥 멤버는 {sample(duty_member_list,3)} 입니다."
        )
        print(response)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'

    return 0
