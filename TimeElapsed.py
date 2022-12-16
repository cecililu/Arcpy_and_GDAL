# timer in python
import datetime
import time
start=time.time()
a=1
while(True):
    current=time.time()
    elapsed = datetime.timedelta(seconds=current-start)
    print ('Time',elapsed)
    a=a+1
