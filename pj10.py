from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('3.10.1', 5500)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") !=  'STOP':
    continue

sender.stop_stream()