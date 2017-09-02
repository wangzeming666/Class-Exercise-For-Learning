import re
import time
bell = input("Enter a ring time(XX:XX:XX):")
while True:
    times = time.ctime()
    m = re.search('\d+:\d+:\d+', times).group()
    if bell in m:
        print("Ring a 'DingDong'")
    time.sleep(1)
