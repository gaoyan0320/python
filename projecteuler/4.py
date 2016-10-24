#coding:utf-8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def twonum():
    for i in xrange(10,100):
        for j in xrange(10,100):
            cheng=i*j
            qian=cheng / 1000
            bai=cheng / 100 %10
            shi=cheng / 10 % 10
            ge=cheng / 1 % 10
            if qian == 0:
                if bai == ge:
                    print i,j,cheng
            else:     
                if qian == ge and bai == shi:
                    print i,j,cheng


# twonum()
def threenum():
    list2=[]
    for i in xrange(100,1000):
        for j in xrange(100,1000):
            cheng = i *j 
            shiwan = cheng / 100000
            wan = cheng / 10000 % 10
            qian = cheng / 1000 % 10
            bai = cheng / 100 % 10
            shi = cheng / 10 % 10
            ge = cheng / 1 % 10
            if shiwan == 0:
                if wan == ge and qian == shi:
                    print i,j,cheng
                    list2.append(cheng)
            else:   
                if shiwan == ge and wan == shi and qian == bai:
                    list2.append(cheng)
    print max(list2)