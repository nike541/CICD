from functions import *
import time
import datetime

print("starting data pipeline at",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("---------------------------------------")

t0 = time.time()
getVideoIDs()
t1 = time.time()
print("Step 1: Done")
print("---> Video IDs downloaded in",str(t1-t0),"seconds","\n")

t0 = time.time()
getVideoTranscripts()
t1 = time.time()
print("step 2: Done")
print("---> Transcript downaloaded in",str(t1-t0),"seconds","\n")

t0 = time.time()
transformData()
t1 = time.time()
print("step 3: Done")
print("-------> Data transformed in",str(t1-t0),"seconds","\n")