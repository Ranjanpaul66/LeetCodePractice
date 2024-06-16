from threading import Thread, current_thread

def disp():
    print("Default child thread name", current_thread().name)

th = Thread(target=disp)
th.start()
th2 = Thread(target=disp)
th2.start()
print("Main thread: ", current_thread().name)

""" To show the thread name 
    here current_thread() return the name  current thread object 
    and here 'name' attribute return the name of thread  
def disp():
    print("Default child thread name", current_thread().name)
    
    
"""


""" Change thread name inside of function"""
def func1():
    print("current thread name before ", current_thread().name)
    current_thread().name = "current TH3"
    print("current thread name will be change ", current_thread().name)

th3 = Thread(target=func1())
th3.start()

""" Change thread name out side of function"""

def func2():
    print("current thread name before ")

th4 = Thread(target=func1)
print("before changed ", th4.name)
th4.name = "Changed Th4 name"
print("after changed ", th4.name)


""" Another way to change the thread name"""
def func3():
    print("current thread name before ")

th4 = Thread(target=func3, name=" New th4 thread")
print("before changed ", th4.name)


import requests