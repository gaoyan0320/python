import os
import re
PWD = os.getcwd()
SEARCH = "this.*"
DIRNAME = "E:\\test.txt"
FILENAME = ['\\test\\test123', 'asdf']

def filefind():
    for i in FILENAME:
        FILE = DIRNAME + i
        print FILE


def allfind():
    pass


def searchfile():
    with open(DIRNAME, 'r') as f:
        aa = f.read()
    str1 = re.findall(SEARCH, aa)
    with open(str1, 'w') as w1:
        w1.write(i + "\n")
if __name__ == '__main__':
    # filefind()
    searchfile()
    # pass
