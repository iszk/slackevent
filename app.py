from chalice import Chalice

import os
import json
import urllib.request
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Chalice(app_name='slackevent')

@app.route('/', methods=['GET'])
def index():
    return {'hello': 'world'}

@app.route('/', methods=['POST'])
def hoge():
    data = app.current_request.json_body
    if (data['type'] == 'url_verification'):
        return url_verification(data)
    elif (data['type'] == 'event_callback'):
        if (data['event']['type'] == 'emoji_changed'):
            return emoji_changed(data['event'])
    log.warn("unsupported data %s" % data)
    return {
        'unsupported': data
    }

def url_verification(data):
    if (data['token'] == os.environ["VERIFICATION_TOKEN"]):
        return {
            'challenge': data["challenge"]
        }

    return {}

def emoji_changed(event):
    if event['subtype'] == 'add':
        """
        data sample (https://api.slack.com/events/emoji_changed)
        {
            "type": "emoji_changed",
            "subtype": "add",
            "name": "picard_facepalm",
            "value": "https://my.slack.com/emoji/picard_facepalm/db8e287430eaa459.gif",
            "event_ts" : "1361482916.000004"
        }
        """
        post = {
            'attachments': [
                {
                    'title': event['name'],
                    'image_url': event['value']
                }
            ]
        }
        url = os.environ["SLACK_WEBHOOK_EMOJI_CHANGED_URL"]
        post_slack(url, post)
    return {}

def post_slack(url, data):
    headers = {
        'Content-Type': 'application/json',
    }

    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return
