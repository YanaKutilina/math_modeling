def changer(a,b):#chainger(a:int,b:list)
  a=2
  b[0]='Good'
  
x=10#неизменяемый тип данных
L=[1,2]#изменяемый тип данных

changer(x,L)

print(x)
print(L)

L = [1, 2]
changer(x, L[:])#чтобы список не изменился
 
print(L)

x = 3
y = 4

z = complex(x,y)#комплексные числа (вектор)
print(z)

w = complex(y, x)

print(z + w)

s = 'hello'
print(s[0])

#changer(3,s) в строках нельзя менять данные

t = (1, 4, 9) #turple неизменяемый список
print(t)#кортедж
print(t[0])

# list список
l = [1, 4, 9]
l[0] = 3
print(l)

# Dict словари
d = {'a1':4, 4:'a1', 'str':'Hello'}
print(d['a1'])
print(d[4])
print(d['str'])

d['str'] = 'Good'
print(d)

