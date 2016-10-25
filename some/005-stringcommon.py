s = ('ttt')
print type(s)
print isinstance(s, unicode)
print s.isalpha()
print s.isalnum()
str1 = ("a", "b", "c")
str2 = ("a", "b", "c")
a = ""
print a.join(str1)
print ''.join(str1)
string3=" DDDabcdefgh"\
    "ijkabcssss       ss "
print tuple(string3)
# print tuple(string3)+list(string3
print string3.startswith("2")
print string3.endswith("12")
print string3.rindex("s")
print "s" in string3
print string3.replace("s","d")
print string3.partition("cssddd")
print string3.rpartition("ceeeeeWG")
print string3.splitlines()
print string3.rsplit(" ")
print string3.rsplit()
print string3.capitalize()
print string3.swapcase()
import string
print string.capwords(string3)
print string3[::-1].strip()
print "##"  

print string3.center(100)
print string3.expandtabs(5000)


print sorted(string3.split())
# print string3.sort()
list1=[1,2,9,4,"1","3","5"]
# print list1.sort()
print sorted(list1)
# print 
print list1