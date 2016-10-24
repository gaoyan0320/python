# coding:utf-8
# python2

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

print "A1"


def A1(a=3, b=5, c=1000):
    sumcount = 0
    for i in xrange(1, c):
        if i % a == 0 or i % b == 0:
            sumcount = sumcount + i
    return sumcount
print A1()

print "A2"


def A2(a=3, b=5, c=1000):
    suma = 0
    sumb = 0
    sumc = 0
    multa = c / a
    multb = c / b
    multc = c / (a * b)
    print multa, multb, multc
    for i in xrange(1, multa + 1):
        suma = suma + (i * a)
    for j in xrange(1, multb):
        sumb = sumb + (j * b)
    for k in xrange(1, multc + 1):
        sumc = sumc + (k * (a * b))
    print suma, sumb, sumc
    print suma + sumb - sumc
A2()

print "A3"
print sum([x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0])
