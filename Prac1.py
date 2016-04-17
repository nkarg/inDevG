# -*- coding: utf-8 -*-

var1 = input ("ingrese el anio de su nacimiento: ")
var2 = input ("ingrese el anio en el que desaria saber su edad: ")
var3 = var2 - var1
print "En el anio ", var2, " usted tendra ", var3, " anios."
print "--------------" #EJERCICIO2
var1 = input ("Ingrese el monto al que desea calcular el IVA: ")
var2 = 21.0 / 100
var3 = ((var1 * var2) + var1)
print "El monto con el IVA incluido es un total de: ", var3
print "--------------"#EJERCICIO3
pres1 = input ("Ingrese el valor de la presion: ")
vol1 = input ("Ingrese el valor del volumen: ")
temp1 = input ("Ingrese el valor de la temperatura: ")
masa = (pres1 * vol1) / (0.37 * (temp1 + 460))
print "El calculo de la masa dio como resultado: ", (round(masa, 1))
print "--------------"#EJERCICIO4
var1 = input ("Ingrese el salario del empleado: ")
var2 = 25.0/100
var3 = (var1 * var2) + var1
print "El nuevo salario del empleado sera de: ", var3, " pesos."
print "--------------"#EJERCICIO5
var1 = input ("Ingrese el monto del presupuesto anual: ")
od1 = 40.0/100
ped1 = 30.0/100
trau1 = 30.0/100
print "El area de Odontologia recibira: ", (var1 * od1), " pesos. El area de Pediatria recibira: ", (var1 * ped1), " pesos. El area de Traumatologia recibira: ", (var1 * trau1), " pesos"
print "--------------"#EJERCICIO6
var1 = input ("ingrese el valor del articulo: ")
var2 = 30.0/100
var3 = (var1 * var2) + var1
print "el articulo deberia venderse en: ", var3, " pesos para obtener ganancias"
print "--------------"#EJERCICIO7
inv1 = input ("primer inversor ingrese el monto que desea invertir: ")
inv2 = input ("segundo inversor ingrese el monto que desea invertir: ")
inv3 = input ("tercer inversor ingrese el monto que desea invertir: ")
totalinv = inv1 + inv2 + inv3
print "el inversor 1 aportara en un ", ((inv1 * 100)/totalinv), " porciento del total, el inversor 2 aportara en un ", ((inv2 * 100)/totalinv), " porciento del total y el inversor 3 invertira en un ", ((inv3 * 100)/totalinv), " porciento"
print "--------------"#EJERCICIO8
print "A continuacion detallaremos el promedio alcanzado por el alumno"
mate_exa = input ("ingrese el valor obtenido en el examen de matematica: ")
mate_ta1 = input ("ingrese el valor obtenido en la primer tarea de matematica: ")
mate_ta2 = input ("ingrese el valor obtenido en la segunda tarea de matematica: ")
mate_ta3 = input ("ingrese el valor obtenido en la tercer tarea de matematica: ")
print "-- Procesando datos .. .. --"
print "-- Proceso listo -- "
fisi_exa = input ("ingrese el valor obtenido en el examen de fisica: ") 
fisi_ta1 = input ("ingrese el valor obtenido en la primer tarea de fisica: ")
fisi_ta2 = input ("ingrese el valor obtenido en la segunda tarea de fisica: ")
print "-- Procesando datos .. .. --"
print "-- Proceso listo -- "
quimi_exa = input ("ingrese el valor obtenido en el examen de quimica: ")
quimi_ta1 = input ("ingrese el valor obtenido en la primer tarea de quimica: ")
quimi_ta2 = input ("ingrese el valor obtenido en la segunda tarea de quimica: ")
quimi_ta3 = input ("ingrese el valor obtenido en la tercer tarea de quimica: ")
print "-- Procesando datos .. .. --"
print "-- Proceso listo -- "
print "--- --- --- --- ---"
totma1 = 90.0/100
totma2 = 10.0/100
prom_ma = (mate_exa * totma1) + (((mate_ta1 + mate_ta2 + mate_ta3) / 3) * totma2)
totfi1 = 80.0/100
totfi2 = 20.0/100
prom_fi = (fisi_exa * totfi1) + (((fisi_ta1 + fisi_ta2) / 2) * totfi2)
totqui1 = 85.0/100
totqui2 = 15.0/100
prom_qui = (quimi_exa * totqui1) + (((quimi_ta1 + quimi_ta2 + quimi_ta3) / 3) * totqui2)
promedio_g = (prom_qui + prom_fi + prom_ma) / 3
print "*** RESULTADOS ***"
print "el alumno a obtenido un promedio general de: ", promedio_g
print "en matematica obtuvo un promedio de ", prom_ma
print "en fisica obtuvo un promedio de ", prom_fi
print  "y en quimica obtuvo un promedio de ", prom_qui
#inicio>equipo>propiedades>configavdesistema>variableysdeentorno>path>;C:\Python27\;C:\Pthon27\Scripts;
#https://docs.python.org/2/library/functions.html