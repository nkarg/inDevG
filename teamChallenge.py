# -*- coding: UTF-8 -*-

print("Imagen 1")
a = ["python", "poo", 999,666]
print (a)
a[2] = 900
a[3] = 600
print (a)

print("Imagen 2")
a = [9, 99, 999,9999]
print (a)
a.remove(9)
a.remove (999)
print (a)

print("Imagen 3")
a = [4, 43, 432,4321]
print (a)
a[0] = 432
a[1]="info2016"
a[2] = "mod1"
print (a)

print ("Imagen 5")
a =["no se nada","no se nada","no se nada"]
print (a)

print ("Imagen 7")
a = ["resistencia", "Corrientes", "Posadas", "Parana"]
print(a)
print (a[3])
a.remove("Parana")
print (a)

print("Imagen 9")
a = [1990,1993,1987,1990,1988,1993,2004,2014,2014,2014,2000,2016,2016]
print (a)
a.sort()
print (a)

print("Imagen 11")
a = ["INFO 2013","INFO 2014"]
print (a)
a.append("INFO 2015")
a.append("INFO 2016")
print (a)

print("Imagen 13")
a = ["A", 1, "B",2,"C", 3]
b = ["A", 1, "B",2,"C"]
print(a)
print(a)
a.remove("A")
print(b)
print(b)

print("Problema 15")
a = [1,2,3,4,5,6,7,8,9,10]
print (a)
a.reverse()
print (a)

print("Problema 17")
a = [1, 2 , 5]
print(a)
a.remove(1)
print (a)

print("Problema 18")
a = ["HOLA ", "SOY "]
print(a)
b= ["JUAN", " PEDRO"]
print(b)
c = a + b
print(c)