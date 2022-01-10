from threading import *
from time import sleep
class Hello(Thread):
    # Thread class must contain run method. Thread start executing from run method
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    # Thread class must contain run method. Thread start executing from run method
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

# Start method will call run method
t1.start()
t2.start()

# when thread task will end then execute below code
t1.join()
t2.join()
print("Bye")