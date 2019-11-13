'''
def test():
    return [], 200

x, y = test()
print(x, y)
'''
import datetime
import time

current = datetime.datetime.now()
time.sleep(1)
next1 = datetime.datetime.now()
diff = current - next1
sec = diff.total_seconds()
print(sec)