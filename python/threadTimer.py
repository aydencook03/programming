from threading import Timer


count = 0
def printCount():
    Timer(1, printCount).start() #starts a non-blocking timer in a seperate thread 
    global count
    count += 1
    print(count)

printCount()
