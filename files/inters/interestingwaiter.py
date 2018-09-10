import os
import time
import threading

def waiter():
    waiter.finished = False
    while not waiter.finished:
        print 'Waiting...'
        time.sleep(1)
os_thread = threading.Thread(target=waiter)
os_thread.daemon = True
os_thread.start()
return_value = os.system('sleep 4.9')
return_value >>= 8  # The return code is specified in the second byte
waiter.finished = True
time.sleep(3)
print 'The return value is', return_value