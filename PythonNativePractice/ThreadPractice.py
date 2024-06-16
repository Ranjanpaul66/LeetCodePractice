from threading import Thread


def disp(a, b):
    print("Thread Running:", a, b,"\n")


# t = Thread(target=disp, args=(10, 20))
# t.start()

for i in range(5):
    t = Thread(target=disp, args=(10, 20))
    t.start()
