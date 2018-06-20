import datetime

# Create a date and show it
current_date = datetime.date.today()
print(current_date)
print('Year = ' + str(current_date.year))
print('Month = ' + str(current_date.month))
print('Day = ' + str(current_date.day))

print('---------------------------------------')

# Create a datetime and show it
current_datetime = datetime.datetime.now()
print(current_datetime)
print('Year = ' + str(current_datetime.year))
print('Month = ' + str(current_datetime.month))
print('Day = ' + str(current_datetime.day))
print('Hour = ' + str(current_datetime.hour))
print('Minute = ' + str(current_datetime.minute))
print('Second = ' + str(current_datetime.second))

print('---------------------------------------')

# Get the timestamp from a datetime
dt_to_ts = current_datetime.timestamp()
print(dt_to_ts)

print('---------------------------------------')

# Convert a timestamp to datetime
ts_to_dt = datetime.date.fromtimestamp(dt_to_ts)
print(ts_to_dt)