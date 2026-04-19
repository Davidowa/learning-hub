# In this module your going to learn how to work with dates and times in Python
# There are two modules in Python that you can use to work with dates and times:
# 1. time
# 2. datetime

# The time module
# The time module is part of the Python standard library and provides a simple way to work with time.
# It gives you a timestamp

# This time module have a method called time() that returns the current time in seconds since the epoch
# Depending on the operating system, the epoch is January 1, 1970, on Unix or January 1, 1601, on Windows

# Example

from datetime import datetime, timedelta
import time

seconds = time.time()
print(seconds)

# We usually work with dates in a more human-readable format
# To convert a timestamp to a date, you can use the fromtimestamp() method
# Example

local_time = time.ctime(seconds)
print(local_time)

# Now, the main functionallity of the time module is to work with the time in seconds
# In programming, we want to know the amount of time that has passed after a certain event
# Usually, we want to measure the time it takes to execute a piece of code

# Example
# Let's say we want to measure the time it takes to "send" 100,000,000 emails


def send_email(emails):
    for email in range(emails):
        pass  # Let's pretend we are sending an email


start_time = time.time()
send_email(100000000)
end_time = time.time()

duration = end_time - start_time

# In this case its printing 0 seconds. If we want to see more decimal places we can use the format method
print(f"Duration: {duration} seconds")
print(f"Duration: {duration:.2f} seconds")

# The datetime module
# This module allows you to work with datetime objects
# A datetime object is a date and time object


# You can create a datetime object by passing the year, month, day, hour, minute, second, and microsecond arguments
# Optionally, you can pass the hour, minute, second, and microsecond arguments
d = datetime(2020, 1, 1)
now = datetime.now()  # This will return the current date and time

# Some times you will need to convert a string to a datetime object
date_string = "2020/01/01"
# This will return a datetime object
# The second argument is the format of the date string
date_object = datetime.strptime(date_string, "%Y/%m/%d")
# There are different format codes that you can use to specify the format of the date string
# You can find the list of format codes in the Python documentation
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# Sometimes you will work with the time module and the datetime module at the same time

# This will return the current date and time
dt = datetime.fromtimestamp(time.time())
print(dt)

# The datemtime object lets you access the year, month, day, hour, minute, second, and microsecond

# Example

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

# When you use the datetime module, you can use the timedelta class to represent a duration
# Let's say we want to know the date and time 3 days from now

# This will return the current date and time
dt = datetime.now()
# This will return the date and time 3 days from now
three_days = datetime.now() + timedelta(days=3)
print(three_days)

# We can use the strftime() to convert a datetime object to a string
# This method takes one argument, which is the format of the date string
# Example
print(datetime.strftime(dt, "%m/%Y"))

# Lastly, one of the main advantages of the datetime modules is that it allows you to use comparison operators

# Example

date1 = datetime(2020, 1, 1)
date2 = datetime.now()

if date1 < date2:
    print("Date1 is in the past")
else:
    print("Date1 is in the future")

# Even you can use arithmetic operations with datetime objects
# Example

date1 = datetime(2020, 1, 1)
date2 = datetime.now()

duration = date2 - date1
print(duration)
print(duration.total_seconds())
