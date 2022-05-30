import csv
import json
from daterange import unix_start_date, unix_end_date

def engagement_counter():
    """
    To use this function, you need to have exported the conversation history from Slack
    to a JSON file with the exact name "conversations.json". 
    You must also edit this file's start_date and end_date variables to the desired range.
    This function will return a .csv with the following columns (for each message):
        'timestamp', 'emoji_count', 'reply_count')
    """

    timed_messages = []
    emojis = {}
    replies = {}
    msg_text = {}

        # Load the message history from the JSON file
    with open('conversations.json', 'r') as f:
        data = json.load(f)
        
        # To get a list of all messages within the predetermind time frame (in Unix time)   
    for message in data:
        
        for key, value in message.items():
            if key == "ts":
                if int(float(value)) >= unix_start_date and int(float(value)) <= unix_end_date:
                    timed_messages.append(message)
                else:
                    pass
                    
    # To get the timestamp and number of emojis in each message as well as the number of replies (unique users).
    for message in timed_messages:
        timestamp = message["ts"]
        count = 0
            
        try:      
            for value in message["reactions"]:
                count += value["count"]        
            emojis[timestamp] = count   
        except:
            pass   
        
        try:    
            replies[timestamp] = message["reply_users_count"]
        except:
            pass
        
        try:    
            msg_text[timestamp] = str(message["text"])
        except:
            pass
                
    # Currently if a message has reactions but no replies, our script still returns it but shows replies as 0
    # However, if a message has replies but no reactions, the script will not return any result for this and skip it
    # Because most (if not all) messages that have replies have reactions, this is not a problem
    header = ['timestamp', 'emoji_count', 'reply_count', 'message_text']
    with open('engagement_count.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for key, value in emojis.items():
            writer.writerow([key, str(value), (str(replies[key]) if key in replies else "0"), (msg_text[key] if key in replies else "")])
            
    print("Successfully exported engagement count to engagement_count.csv")
    print("Total Number Of Messages with Reactions:", len(emojis))

    # Run the function
engagement_counter()    