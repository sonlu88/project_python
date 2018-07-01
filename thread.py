import thread
 
def someFunc():
    print "someFunc was called"
 
thread.start_new_thread(someFunc, ())