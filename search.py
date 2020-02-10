import sys
import re

from time import mktime
from datetime import datetime

# truncate the file name and collect all args passed in cli
args = sys.argv[1:]

def date_to_timestamp(datetime_str):
    return mktime(datetime.strptime(datetime_str, "%d/%m/%Y %H:%M").timetuple())

def time_validator(time):
    # check if time matches format
    is_time_format = bool(re.match('[0-9]{1,2}:[0-9]{2}$', time))

    if not is_time_format:
        print("Invalid Time: The format for Time is not right!")

    return is_time_format

def date_validator(date):
    # check if date matches format
    is_date_format = bool(re.match('([0-9]{1,2}-{1}){2}[0-9]{4}$', date))

    if not is_date_format:
        print("Invalid Date: The format for date is not right!")
    
    return is_date_format


def search(start_date, start_time, end_date, end_time):
    if end_time is None:
        end_time = '23:59'
    
    for transaction in DATA:
        datetime_str = transaction['time']

def main():
    # initialize variables
    start_date = start_time = end_date = end_time = None

    # re-assign to args passed
    if len(args) == 1:
        end_date = args[0]
    
    elif len(args) == 4:
        start_date, start_time, end_date, end_time = args

    else:
        print('No Arguments supplied')
    
    print(start_date, start_time, end_date, end_time)
    search(start_date, start_time, end_date, end_time)

if __name__ == "__main__":
    main()
