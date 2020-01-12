"""
Multi-threading: Execute a program simultaneously using multiple threads.
"""

from time import *
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()
"""
t1.run()
t2.run()
"""
t1.start()
sleep(.2)
t2.start()

t1.join()
t2.join()
print("Bye")
