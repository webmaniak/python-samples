import datetime

class TimeRecorder():
    """Records the elapsed time between the enter and exit statements."""

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.delta_time = None
    
    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.datetime.now()
        self.delta_time = self.end_time - self.start_time
        print("Elapsed time: " 
                + str(self.delta_time.seconds)
                + "." 
                + str(int(self.delta_time.microseconds / 1000))
                + "s")

# Example of usage:
# with TimeRecorder() as t:
#     counter = 1
#     while counter < 10000000:
#         counter += 1
