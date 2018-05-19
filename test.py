import datetime

start = datetime.datetime.now()
print(start)

counter = 1
while counter < 100000:
    counter += 1

end = datetime.datetime.now()
delta = end - start
print(delta)