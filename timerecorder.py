from contextlib import contextmanager
import datetime

@contextmanager
def measure(counter):
    try:
        start = datetime.datetime.now()
        yield start
    finally:
        end = datetime.datetime.now()
        delta = end - start
        print("Elapsed time: " + str(delta.seconds) + "." 
                + str(int(delta.microseconds / 1000)) + "s")

"""
def measure(counter):
    try:
        start_time = time.time()
        #print("Counter started on " + start_time.strftime("%H:%M:%S.%f") + " at value " + str(counter))
    finally:
        end_time = time.time()
        #print("Counter reached end on " + end_time.strftime("%H:%M:%S.%f"))
        print((end_time - start_time))
"""

counter = 1
with measure(counter) as m:
    while counter < 100000000:
        counter += 1

print("Done!")
