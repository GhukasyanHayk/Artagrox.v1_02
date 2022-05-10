
database = {

"x3+6/y2+5+ex+y":

"""import math

x = int(input("X: "))
y = int(input("Y: "))

def Main(x,y):
    verev = x ** 3 + 6
    nerqev = y ** 2 + 5
    
    return verev / nerqev + math.e ** abs(x + y)

print(Main(x,y))"""
,
"logab+cosa2+b2":
"""import math

a = int(input("A: "))
b = int(input("B: "))

print(math.log(b,a) + math.cos(math.sqrt(a ** 2 + b ** 2)))""",
"arctg5x+y":
"""import math

x = int(input("X: "))
y = int(input("Y: "))

print(math.atan(abs(x + y) ** 5))""",
"y=b-1+tg2c+a":
"""import math

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

y = abs(b - 1) + math.tan(c + a) ** 2

print(y)""",

"Trvat e uxankyan A ev B kxomer@ qani qarakusi ktexavorvi B koxmov":
"""import math

a = int(input("A: "))
b = int(input("B: "))

if a > b:
    print(a // b)
else:
    print("Error")""",

"Orva skzbic ancel e n vayrkyan hashvel qani jam rope e ancel":
"""sec = int(input("Enther seconds: "))

sec = sec % (24 * 3600)
hour = sec // 3600
sec = sec % 3600
mini = sec // 60
sec = sec % 60

print(hour,mini , sec)""",

"Trvat e uxankyan erankyan ejer@ hashvel nerqnadiq@":
"""ej1 = int(input("arajin ej: "))
ej2 = int(input("arajin e2j: "))

nerqnadiq = ej1 ** 2 + ej2 ** 2

for i in range(1, nerqnadiq):
    if i * i == nerqnadiq:
        print(i)
        break""",

"Trvat en erku keteri kordinatner@ hashvel nranc mijev exat heravorutyun@":
"""import math

x1 = int(input("X1:"))
y1 = int(input("Y1:"))
x2 = int(input("X2:"))
y2 = int(input("Y2:"))

print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))""",
"Trvat e jam@ ev ropen voroshel jam slaqi kazmat ankyun@ orva skzbic":
"""jam = int(input("Jam: "))
rope = int(input("Rope: "))

print((jam * 60 + rope) / 2)""",
"Trvat e jam@ ev ropen voroshel rope slaqi kazmat ankyun@ orva skzbic":
"""jam = int(input("Jam: "))
rope = int(input("Rope: "))

print(6 * (rope + jam * 60))""",

"Trvat e tvabanakan progresiayi arajin andam@ a1 ev d tarberich@ gtnel tvabanakan progresiayi andam@":
"""a1 = int(input("A1: "))
d = int(input("D: "))
n = int(input("N: "))


print(a1 + d*(n - 1))""",
"Hashvel tvabanakan progresiayi elementneri gumar@ ete trvat e a1-@ d-n n@":
"""a1 = int(input("A1: "))
d = int(input("D: "))
n = int(input("N: "))


print((a1 + (a1 + d*(n - 1))) * (n / 2))""",
"Trvat e erankyan 3 ejer@ hashvel erankyan makeres@ Heroni banadevov":
"""import math

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))


p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(S)""",
"s=EEi*j":
"""m = int(input("M: "))
n = int(input("N: "))

itog_hastat = 0

for j in range(1, m + 1):
    itog = 0
    for i in range(1, n + 1):
        itog += i  * j

    itog_hastat += itog

print(itog_hastat)""",

"s=E1/i=1+1/2+1/3+1/4+1/5+1/n":
"""n = int(input("N: "))
itog = 0

for i in range(1, n + 1):
   itog += 1 / i

print(itog)""",

"s=Ei!=1+1*2+1*2*3+1*2*3n":
"""import math
n = int(input("N: "))
itog = 0

for i in range(1, n + 1):
   itog += math.factorial(i)

print(itog)""",

"s=Pi2Ej+2*i":

"""import math
n = int(input("N: "))
m = int(input("M: "))
itog = 1

for i in range(1, m + 1):
    itogh = 0
    for j in range(1, n + 1):
        itogh += (j+ 2) * i  
    itog *= i ** 2 * itogh    
    
print(itog)""",

"s=EjEj+3*j":
"""import math
n = int(input("N: "))
m = int(input("M: "))
itog = 0

for i in range(1, m + 1):
    itogh = 0
    for j in range(1, n + 1):
        itogh += (j+ 3) * i  
    itog += j * itogh    
    
print(itog)""",
"p=PiEi+j2":
"""import math
n = int(input("N: "))
m = int(input("M: "))
itog = 1

for i in range(1, m + 1):
    itogh = 0
    for j in range(1, n + 1):
        itogh += i + j ** 2  
    itog *= i * itogh    
    
print(itog)""",
"Ex2 x=2 x=3/x-3/":
"""import math
n = int(input("N: "))
x = 2
# m = int(input("M: "))
itog = x ** 2

for i in range(2, n + 1):
    x = 3 * abs(x - 3)
    itog += x ** 2
    
    
    
print(itog)""",

"Px2+x x=2 x=x+3":
"""import math
n = int(input("N: "))
x = 2
# m = int(input("M: "))
itog = x ** 2 + x

for i in range(2, n + 1):
    x = x + 3
    itog *= x ** 2 + x
    
    
    
print(itog)""",

"Ex+y x=1 x=2x+3 y=2 y=y-3":
"""import math
n = int(input("N: "))
x = 1
y = 2
# m = int(input("M: "))
itog = (x + y) ** 2

for i in range(2, n + 1):
    x = 2 * x + 3
    y = y - 3 
    itog += (x + y) ** 2
    
    
    
print(itog)""",

"Ei+3Pj":
"""n = int(input("N: "))
m = int(input("M: "))
itog = 0

for i in range(1, m + 1):
    itogh = 1
    for j in range(1, n + 1):
        itogh *= j  
    itog += (i + 3) * itogh 
    
print(itog)""",

"Trvat e shrjanagti sharavix@ hashvel nra Makeres@":

"""import math

num = int(input("Num: "))


print(math.pi * math.pow(num, 2))""",
"Trvat e shrjanagti sharavix@ hashvel nra erkarutyun@":
"""import math

num = int(input("Num: "))


print((2 * math.pi) * num)""",

"Trvat e n chapani vektor gtnel verjin 2 harevan ayn tareri kargahamarner@ voronq unen tarber nshanner":

"""from random import randint

n = int(input("N: "))
lis = []

count = 0
test = True

for i in range(n):
    lis.append(randint(-9,9))
    if lis[i] > 0 and test:
        count += 1
        test = False
    if lis[i] < 0 and test != True:
        count += 1
        test = True
        

print(lis)
print(count)""",

"Gtnel ev tpel n chapani vektori ayn tarreri qanak@ voronq met en dax ev aj harevan tarreric":

"""from random import randint

n = int(input("N: "))
lis = []

for i in range(n):
    lis.append(randint(1,9))

count = 0

for i in range(1, len(lis) - 1):
    if lis[i - 1] < lis[i] > lis[i + 1]:
        count += 1
print(lis)
print(count)""",

"Str_rand":
"""import random
import string

s = ''.join([random.choice(string.ascii_letters) for n in range(12)])
print(s)""",

"Qarakusun ankyunagter@ bajanum e 4 erankyan":

"""n = int(input("Enther the N: "))

gener = [[0 for i in range(n)] for j in range(n)]

def Main(gener):
    for i in range(n):
        for j in range(n):
            if i < j and j < n - 1 - i:
                gener[i][j] = 1
            if i < j and j > n - 1 - i:
                gener[i][j] = 2
            if i > j and j > n - 1 - i:
                gener[i][j] = 3
            if i > j and j < n - 1 - i:
                gener[i][j] = 4
    printt(gener)
    
    
def printt(gener):
    for i in range(n):
            for j in range(n):
                print(gener[i][j], end = ' ')
            print()
            
Main(gener)""",

"Trvat e n amboxj tiv karucel kargi B matrici hetevyal baxadrichnerov":

"""n = int(input("N: "))
gener = [[0 for i in range(n)]for j in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if i == j:
            count += 1
            gener[i][j] += count
        elif i < j: 
            gener[i][j] += count
            

        print(gener[i][j], end = ' ')
    print()""",

"Trvat e NxN tarr parunakox patahakan generacvat X erkchap zangvat artatel matrici ayn toxi hamar@ vor@ kazmvat e miayn drakan tarreric":
"""from random import randint

n = int(input("N: "))

gener = [[0 for i in range(n)]for i in range(n)]
def Main(gener):
    count = []
    lis = []
    for i in range(n):
        lis = []
        for j in range(n):
            gener[i][j] = randint(-1, 10)
            print(gener[i][j], end = ' ')
            lis.append(gener[i][j])
        if stugum(lis):
            count.append(i)
            
        print()
    return count

def stugum(lis):
    temp = 0
    for i in lis:
        if i < 0:
            return False
    return True


print(Main(gener))""",

"Trvat e NxN tarr parunakox patahakan generacvat X erkchap zangvat poxatexel 1in ev verjin toxer@ ev artatel nor zangvat":

"""from random import randint
n = int(input("N: "))

gener = [[0 for i in range(n)]for j in range(n)]
def Main(gener):
    

    for i in range(n):
        for j in range(n):
            gener[i][j] = randint(0, 9)
            print(gener[i][j],end = ' ')
        print()
    print()

Main(gener)
gener[0], gener[-1] = gener[-1], gener[0]

for i in range(n):
        for j in range(n):
            print(gener[i][j], end = ' ')
        print()""",

"Trvat e NxN tarr parunakox patahakan generacvat X erkchap zangvat hashvel ev artatel matrici poqraguyn tarri toxi ev syan kargahamari gumar@":

"""from random import randint
n = int(input("N: "))

gener = [[0 for i in range(n)]for j in range(n)]
def Main(gener):
    count = 0
    minimal = 100
    for i in range(n):
        for j in range(n):
            gener[i][j] = randint(10, 99)
            print(gener[i][j], end = ' ')
            
            if gener[i][j] < minimal:
                minimal = gener[i][j]
                count = i + j
        print()
    print(minimal,count)
Main(gener)""",

"Trvat e NxN tarr parunakox patahakan generacvat X erkchap zangvat gtnel ojandak ankyunagti vra kam nranic nerqev gtnvox ayn tarreri mijin tvabanakan@ voronq bazmapatik en k amboxj tvin":
"""from random import randint
n = int(input("N: "))
k = int(input("K: "))

gener = [[0 for i in range(n)]for j in range(n)]
def Main(gener, k):
    lis = []
    for i in range(n):
        for j in range(n):
            gener[i][j] = randint(10, 99)
            if j + i == n - 1 or j > n -1  - i:
                if gener[i][j] % k == 0:
                    print(gener[i][j])
                    lis.append(mij(gener[i][j]))
    print()
    print(str(gener).replace("],", "],\n")) 
    return lis
        
def mij(num):
    summ = 0
    step = 0
    while num > 0:
        temp = num % 10
        summ = summ + temp
        num = num // 10
        step = step +  1
    return summ / step

print(Main(gener, k))""",

"1234 2341 3412 4123":

"""matrix = [[1,2,3,4]]
for i in range(1, 4):
    matrix.append(matrix[i-1][1:] + [matrix[i-1][0]])

print(Fore.GREEN + str(matrix).replace("],", "],\n"))""",

"12345 1098765 1112131415 2019181716":

"""matrix = [[i + 5*j for i in range(1, 6)] for j in range(4)]

for i in range(len(matrix)):
    if i % 2:
        matrix[i] = matrix[i][::-1]

print(str(matrix).replace("],", "],\n"))""",

"234567 345678 456789 5678910 67891011 7891011112":

"""matrix = []
for i in range(6):
    matrix.append(list(range(2 + i,8 + i)))

print(str(matrix).replace("],", "],\n"))""",

"123456 24681012 369121518 4812162024 51015202530 61218243036":

"""matrix = []
for i in range(6):
    matrix.append([])
    for j in range(6):
        matrix[i].append(i + 1 + j*(i+1))
print(str(matrix).replace("],", "],\n"))"""
}

for key, value in database.items():
  for _ in range(10):
    value = value.replace("    ", "").replace("\t", "")
  database[key] = value