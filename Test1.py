
#variable declare
var = 'Hello World'
print(var)
print("Welcome is " + var)

#Data type
krity = 'sumit'
print(krity)               #str
me = "Mouno"
print('My name is'+ ' ' + me)

Age = 23
print(type(Age))           #int

cg = 3.8
print(type(cg))            #float

X = 5j
print(type(X))             #complex

Y = range(5)
print(type(Y))             #range

Z = ['apple','mango','licchi']
print(type(Z))             #list

P = ('Mounota','Das','Krity')
print(type(P))

M = {'name':'mounota das', 'age':22}
print(type(M))             #dict

X_Y = False
print(type(X_Y))           #bool

username = 'krity'
id = 1105
print(f"my name is {username} & my class id is {id}")

HabluList = [1,3,4,255]
b = bytes(HabluList)
print(type(b))              #bytes

HabluList1 = [1,2,6,8,19]
b1 = bytearray(HabluList1)
print(type(b1))             #bytearray
b1[1] = 35
print(b1[1])

X = None
print(type(X))               #Nonetype

#Arithmetic Operator
A = 10
B = 53
print(A+B)                   #Add
print(A-B)                   #Sub
print(A*B)                   #Mul
print(B/A)                   #Div
print(A%B)                   #Mod
print(A**B)                  #Exponentiation
print(B//A)                  #Floor Division

#Assignment Operator
X = 20
X+= 10
print(X)

X = 20
X-= 10
print(X)

#Swapping
c = 10
d = 21
c,d = d,c
print("This value is now c =", c)
print("This value is now d =", d)

#User Input
username = input("Enter your username: ")
password = input("Enter your password:krity")

print(username)
print(password)

#List types:-

#AccessList
MyList = ['Mango','Banana','Kamranga','Jolpai']
print(MyList[2])        
print(MyList[1:3])

#ChangeList
MyList = ['Mango','Banana','Kamranga','Jolpai']
MyList[3] = ['Watermelon']
print(MyList)
MyList.insert(1,'Licchi')    #insert
print(MyList)
MyList.append("orange")      #append
print(MyList)
MyList = ['Mango','Banana','Kamranga','Jolpai']
ThisList = ["mango", "pineapple", "papaya"]
MyList.extend(ThisList)      #extend
print(MyList)

#RemoveList
MyList = ['Mango','Banana','Kamranga','Jolpai']
MyList.remove("Jolpai")
print(MyList)        #remove
MyList = ['Mango','Banana','Kamranga','Jolpai']
MyList.pop(2)        #pop
print(MyList)
MyList = ['Mango','Banana','Kamranga','Jolpai']
del MyList[2]        #del
print(MyList)
MyList = ['Mango','Banana','Kamranga','Jolpai']
MyList.clear()       #clear
print(MyList)

#LoopList
LoopList = ['Apu','Porimoni','sabnam','Nihar']
for prem in LoopList:
    print(prem)
for i in range (len(LoopList)):    #using range & length
    print(i)

LoopList = ['Apu','Porimoni','sabnam','Nihar']
i = 1
while i < len(LoopList):
    print(LoopList[i])
    i = i + 1

#SortList
number = [3,2,6,5,10]
number.sort()
print(number)
number.sort(reverse=True)
print(number)

#CopyList
number = [3,2,6,5,10]
number.copy()
print(number)
number = [3,2,6,5,10]
number2 = number.copy()
print(number2)

#Join 2List
num1 = [1,2,3]
num2 = [4,5,6]
num3 = num1 + num2
print(num3)
num1.extend(num2)
print(num1)

#Matrix
Hablu = [
    [1,4,'krity',80],
    ['jh',9,7],
    8765
]
print(Hablu[0][2])
print(Hablu[1][2])

#TupleTypes
thistuple = ("apple", "banana", "cherry")
print(type(thistuple))
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
thistuple = ("apple", "banana", "cherry")
print(thistuple[-2])

#update tuple
x = ('apple','banana','cherry')
y=list(x)
y[1]='kiwi'
x=tuple(y)
print(x)
ThisTuple = ("Anarosh","Tomatoo","Banana")
w = list(ThisTuple)
w.append("Brinjal")
ThisTuple = tuple(w)
print(ThisTuple)

#Update Tuple
ThisTuple = ("Eshan","HAblu","Tutul")
a = list(ThisTuple)
a[1] = "Gablu"
a.append ("Shakil")
print(a)

#Unpack Tuple
fruits = ('apple','banana','licchi','cherry')
(a,*c,d) = fruits
print(c)

#loop Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

thistuple2 = ("apple", "banana", "cherry")
for i in range(len(thistuple2)):
    print(thistuple2[i])

thistuple3 = ("apple", "banana", "cherry")
i = 1
while i < len(thistuple3):
    print(thistuple3[i])    
    i = i + 1

#Join Tuples
tuple1 = ('a','b','c')    
tuple2 = ('d','a','e')
tuple3 = tuple1 + tuple2
print(tuple3)

num = 1,2,3,4
print(num*2)

#Set
MySet = {'Mouno','Das','Krith'}
print(type(MySet))

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#Add
Myset1 = {'eshan','hablu','tutul'}
Myset1.add('krith')
print(Myset1)

thisset = {'apple','banana','kamranga'}
tropical = {'mango','papaya'}
thisset.update(tropical)
print(thisset)

#Remove Set
Myset = {'eshan','hablu','tutul'}
Myset.remove('eshan')
print(Myset)

Myset = {'eshan','hablu','tutul'}
Myset.discard('hablu')          #discard
print(Myset)

Myset = {'eshan','hablu','tutul'}
Myset.pop()
print(Myset)

Myset = {'eshan','hablu','tutul'}
Myset.clear()
print(Myset)

#Loop
ThisSet = {'apple','banana','kamranga'}
for k in ThisSet:
    print(k)

#Join Set
set1 = {'a','b','c'}
set2 = {2,4,6}
set3 = set1.union(set2)            #union
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)         #intersection- maan same tai dhrbe
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)        #intersection_update
print(set1)

#Dictionaries
MyInfo= {
    "Krityy" : {
        'Location' : 'Askardighi',
        'Study'    : '3rd Year',
        'Subject'  : 'Science',
        'Roll'     : '0222220005101105'
    },
    "Mouno"  : {
        'Location' : 'Germany',
        'Study'    : 'Masters',
        'Subject'  : 'AI related'
    }
}
print(MyInfo)
print(MyInfo['Krityy']['Study'])

#Accessing items
X = MyInfo.get('Mouno')
print(X)

Y = MyInfo.keys()
print(Y)

MyInfo.values()
print(MyInfo.values())
 
#update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#remove
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("brand")
print(thisdict)

MyDict = {
    'Brand' : 'Alion',
    'Model' : 'Mustang',
    'Year'  : '2021'
}
MyDict.popitem()
print(MyDict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

ThisDict = {
    'Home' : 'Askardighi',
    'City' : 'Ctg',
    'Year' : '2003'
}
for x in ThisDict:
    print(ThisDict[x])

ThisDict = {
     'Home' : 'Jamalkhan',
    'City' : 'Chittagong',
    'Year' : '2003'
}  
for x in ThisDict.values():
    print(x)

MyDict = {
    'Name' : 'Mounota',
    'Age'  : '22',
    'ID'   : '0222220005101105',
    'Sec'  : 'C'
}
for x in MyDict.keys():
    print(x)
    
for x in MyDict.items():
    print(x)

#Copy
MyDict = {
    'Name' : 'Mounota',
    'Age'  : '22',
    'ID'   : '0222220005101105',
    'Sec'  : 'C'
}
Z = MyDict.copy()
print(Z)

R = dict(MyDict)
print(R)

#While
krity = 0
while krity < 20:          #using while
    print(krity)
    krity += 1

i = 1
while i < 8:
    print(i)
    if i == 4:
        break             #using break
    i += 1

i = 1
while i < 8:
    i += 1
    if i == 4:
     continue  
    print(i)           #using continue

#For loop
fruits = ['apple','banana','cherry']
for u in fruits:       #using for
    print(u)

for x in "cherry":
    print(x)

fruits = ['apple','banana','cherry']
for u in fruits:       #using for
    print(u)
    if u == "apple":
        break          #using break
 
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(5):
    print(x)

#Function
def HabluFun(a,b):
    sum = a + b
    print(sum)
HabluFun(20,15)
HabluFun(81,22)

def Minus(x,y):
    sub = x - y
    print(sub)
Minus(30,10)

def my_function(name):
    print(name +" "  + "Das")
my_function("Mounota")

#Recursion
#def ReFun():
    #print("Hablu")
    #ReFun()
#ReFun()

#Zip Function
List1 = ["Mouno","Ripa","Srija"]
List2 = ["Shibu","Arush","Sristy"]
print(list(zip(List1,List2)))

#Debugging
i = 0
while i < 10:
    print(i)         #means every step define kra
    i = i + 1

#Lambda
x = lambda a : a + 10
print(x(7))

y = lambda a,b : a * b
print(y(6,9))

#Array
MyArray = ["eshan","hablu","tutul"]
MyArray[2] = "Joy"
print(MyArray)
 
#Class & Object
class Hablu:
    name = ""
    Number = ""

a = Hablu()
b = Hablu()
a.name = "eshan"
a.Number = "013087"
b.name = "Krity"
print(a.name)
print(a.Number)
print(b.name)

#Inheritance
class baba():           #Parent class 
    car = "BMW"
    Home = "Jumairah"
    Floor = "10th"

class kaka(baba):      #Child class
    BrokenPhone = "?"
    BrokenHome = ""

a = kaka()
print(a.car)        

b = baba()
print(b.Home)

#Multiple inheritence
class baba():           #Parent class 
    car = "BMW"
    Home = "Jumairah"
    Floor = "10th"

class baba1():
    Watch = "Neviforce"
    model = "realme 9"


class kaka(baba,baba1):      #Child class
    BrokenPhone = "?"
    BrokenHome = ""

a = kaka()    
print(a.model)

#iterator
list = [1,2,3,"Eshan","Hablu"]
x =  iter(list)
print(next(x))
print(next(x))