import time
import datetime

"""
Start and End dates for use in the bot.py script and emojicounter.py function.
"""

### +++++++++++++++++ ###
### EDIT THIS SECTION ###
### +++++++++++++++++ ###

# Start Date (if single digit day/month, DO NOT include a leading zero)
s_day = 18
s_month = 5
s_year = 2022

# Start Date (if single digit day/month, DO NOT include a leading zero)
e_day = 19
e_month = 5
e_year = 2022


### =========================== ###
### DO NOT EDIT BELOW THIS LINE ###
### =========================== ###

    # Set start and end dates for messages to be counted (in YYYY-MM-DD format)
utc_start_date = datetime.datetime(s_year, s_month, s_day)
utc_end_date = datetime.datetime(e_year, e_month, e_day)

    # Converts start and end dates to Unix time (DO NOT EDIT THIS)
unix_start_date = int(float(time.mktime(utc_start_date.timetuple())))
unix_end_date = int(float(time.mktime(utc_end_date.timetuple())))
