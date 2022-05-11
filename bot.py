import slack
import logging
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack_sdk.errors import SlackApiError
from emojicounter import emoji_counter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)

client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
BOT_ID = client.api_call("auth.test")["user_id"]

#logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

#@slack_event_adapter.on("message")
#def message(payload):
#    print(payload)
#    event = payload.get("event", {})
#    channel_id = event.get("channel")
#    user_id = event.get('user')
#    text = event.get('text')
#    
#    if BOT_ID != user_id:
#        client.chat_postMessage(channel=channel_id, text=text)
        
# Store conversation history
conversation_history = []
# ID of the channel you want to send the message to
channel_id = "C03ERHU5YBD"

try:
    # Call the conversations.history method using the WebClient
    # conversations.history returns the first 100 messages by default
    # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
    result = client.conversations_history(channel=channel_id)

    conversation_history = result["messages"]

    # Print number of messages in the channel
    logger.info("{} messages found in {}".format(len(conversation_history), channel_id))
    print("{} messages found in {}".format(len(conversation_history), channel_id))
    
    with open('conversations.json', 'w') as outfile:
        json.dump(conversation_history, outfile)
    
except SlackApiError as e:
    logger.error("Error creating conversation: {}".format(e))



if __name__ == "__main__":
    app.run(debug=True)
    emoji_counter()