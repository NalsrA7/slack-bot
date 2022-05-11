import json
import time
import datetime
from collections import Counter

    # Set start and end dates for messages to be counted (in YYYY-MM-DD format)
start_date = datetime.datetime(2022, 5, 11)
end_date = datetime.datetime(2022, 5, 12)

timed_messages = []
emojis = []

    # Initialize the message history from the file
with open('conversations.json', 'r') as f:
    data = json.load(f)
    
    # To get a list of all messages within the predetermind time frame (in Unix time)   
unix_start_date = int(float(time.mktime(start_date.timetuple())))
unix_end_date = int(float(time.mktime(end_date.timetuple())))

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
            
            for key2, value2 in value[0].items():
                if key2 == "name":
                    emojis.append(value2)
        
        else:
            pass
            
emojis_count = Counter(emojis)
print(emojis_count)

