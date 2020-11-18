name = 'rachit shukla'
l=len(name)
print('length is',l)
print(name[0])
print(name[7])
print(name[0:8])
print(name[-1])
print(name[-5])
print(name[-1: :-1]) #printing name in reverse, mid one is end(left coz want full), last is direction
print(name.capitalize())
print(name.title())
print(name.isdigit())
items=[24,78,90,56,79,81]
print(items[1])
print(items[3])
del items[0]
print(items)
print(items[0:4])
items.append(99)
print(items)
items.insert(0,'dude')
print(len(items))
items.remove(56)
print(items)
lizt=[1,22,4,55,6,77]
print(min(lizt))
print(max(lizt))
# loop: column wise aayega sab
for x in lizt:
    print(x)
lizt.reverse()
print(lizt)
ztup=(333,45,78,99,87)
print(ztup)
print(ztup[1])
# dictionary
data={'name':'rachit','address':'bhopal','phone':95763}
print(type(data))
print(data)
print(data['name'])
print(data['address'])
print(data['phone'])
for key in data.items():
    print(key)
for key in data.keys():
    print(key,'=>',data.get(key))
# set: only prints unique items
my_set={11,22,44,55,66,22,88,67,33,11,55,9}
print(type(my_set))
print(my_set)
# control statements:(to control flow of prog) if, else, for, while, break
n=50
if n>45: print(n)
x=3
if x>0: print(x,'is positive value')
elif x<0: print(x,'is negative value')
else: print(x,'is zero')
## agar hellow world 5 times print karna ho:
for i in range(0,5):
    print('hello world')
    print(i)
##reverse chalaane k liye..10 se 1 tak:
for j in range(10,0,-1):
    print(j)
lyzt=[11,23,45,67,88,99,90]
print(len(lyzt))
s=0
for x in lyzt:
    s=s+x
print('sum=',s)
##while loops runs jabtak condition true hoti hai, false hote hi it breaks:
##agar print karna ho aur count karna ho saari digits:
n=599 # or take int(input('enter num: '))
c=0
sm=0
while(n>0):
    r=n%10
    c+=1
    sm=sm+r #or sum+=r
    n = n // 10  # taaki decimals mein na ho n ki val
print('count: ',c) #counts number of digits
print('sum: ',sm)

## to print nums from 1 to 10 using while loop:
i=0
while(i<=10):
    print(i)
    i=i+1 #or i+=1
#to print 1 to 100:
while(i<=100):
    print(i)
    #if u wanna break loop after 50
    if i==50:
        break
    i+=1
print('loop ended')
#to print these 3 lines 10 times:
for i in range(1,11):
    print('1st line')
    print('2nd line')
    print('3rd line')
    print('+++++++++')
#doing something different:
for i in range(1,11):
    print('1st line',i)
    if i==2:
        continue
    print('2nd line')
    print('3rd line')
    print('+++++++++')
## functions:
def fun1():
    print('this is my 1st function')
fun1() #calling fn is imp otherwise nothing prints
def sayHello(name):
    print('hello',name)
sayHello('Rax')
def sayHello(name='no name'):
    print('hello',name)
sayHello() #if nothing is given then no name will be printed
def doSum(a,b):
    return a+b
ans=doSum(45,90)
print(ans)
import math #another way is to write 'from math import *'
# this will import all and we don't have to write math<dot> again and again below
print(math.sqrt(16))
print(math.pow(2,2))
print(math.ceil(343,43))