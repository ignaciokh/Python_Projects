import time
import psutil
from datetime import datetime

start = psutil.net_io_counters()

while True:
    net = psutil.net_io_counters()
    now = datetime.now().strftime("%H:%M")
    
    uploaded = net.bytes_sent - start.bytes_sent
    downloaded = net.bytes_recv - start.bytes_recv
    
    print(now, uploaded, downloaded)
    
    time.sleep(60)