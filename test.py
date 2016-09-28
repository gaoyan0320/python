import os
ret=os.fork()
if ret ==0 :
    print "chiledre"
    print os.getpid()
else:
    print "parent"
    print os.getpid()
print os.getpid()