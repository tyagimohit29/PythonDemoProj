from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(1)

obj1 = Hello()
obj2 = Hi()

obj1.start()
sleep(.5)
obj2.start()

obj1.join()
obj2.join()
print('bye')

