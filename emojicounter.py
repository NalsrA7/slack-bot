import json
from collections import Counter
from daterange import unix_start_date, unix_end_date

def emoji_counter():
    """
    To use this function, you need to have exported the conversation history from Slack
    to a JSON file with the exact name "conversations.json". 
    You must also edit this file's start_date and end_date variables to the desired range.
    This function will return a dictionary with the following structure:
        Counter({'emoji_name1': 4, 'emoji_name2': 2, ...})
    """

    timed_messages = []
    emojis = []

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
                    
        # To count (and return) how many times a certain emoji is used in message history within time frame
    for message in timed_messages:
        
        for key, value in message.items():
            if key == "reactions":
                
                for i in value:
                    for key2, value2 in i.items():
                        if key2 == "name":
                            emojis.append(value2)
            
            else:
                pass
                
    emojis_count = Counter(emojis)
    print(emojis_count)

    # Run the function
emoji_counter()    