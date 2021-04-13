# домашка с пояснениями
def myfunc():
    myfunc=(open('C:\\Users\\Я\Desktop\\pyton(1)\\111.txt'))
    nums=[]
    for i in myfunc:
        print(nums.append(i[:-1]))
    print({c:nums.count(c) for c in nums})
print(myfunc())
mystring=str("eyi")
def ispalindrome(mystring):
    return mystring==mystring[::-1]
print(ispalindrome(mystring))
c='Hello Baby'
m=''
t=''
for i in c:
    if i.isupper():
        m+=i.upper()
    else:
        t+=i.lower()
k=c.count(' ')
print(len(m))
print(len(t))
print(k)
d={'upper':len(m),'lower':len(t)-k}
print(d)
print(d)
