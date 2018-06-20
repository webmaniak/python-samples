import time

# Display current time
current_time = time.time()
print(current_time)

# Wait for 3.5 seconds
#time.sleep(3.5)

# Compare new timestamp with previous one
next_time = time.time()
print(
    'Difference between previous and next time is: '
    + str(next_time - current_time)[0:5]
    + "s")

# Get localtime (with date) and display the current year
local_time = time.localtime()
print(local_time)
print(local_time.tm_year)

# Transform a timestamp into a displayable date and back
print(current_time)
current_loc_date = time.localtime(current_time)
print(current_loc_date)
current_loc_date_sec = time.mktime(current_loc_date)
print(current_loc_date_sec)

# Format a timestamp into a nice human-friendly string
print(time.strftime('%d.%m.%Y %H:%M', current_loc_date))