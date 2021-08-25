import datetime

def timed_proc():
    text = input()

start_time = datetime.datetime.now()
print("Input: the lazy fox jumps over the brown dog")
timed_proc()
time_taken = datetime.datetime.now() - start_time
print(time_taken)
