import time
from ex_7_25__clockdeco_param import clock


@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze(0.123)
