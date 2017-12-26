import threading

class BuckyMessager(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = BuckyMessager(name = "send out messages")
y = BuckyMessager(name = "Recieve messages")
x.start()
y.start()