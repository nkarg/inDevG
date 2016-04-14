# -*- coding: utf-8 -*-

print "## PARES E IMPARES ##"
var1 = input ("Ingrese el valor que desea evaluar: ")
print "-- Evaluando --"
if (var1 % 2) == 0:
	print "El numero ingresado es par"
else:
	print "El numero ingresado es inpar"
print " ----- "
print " ----- "
print "## Mayores al promedio ##"
var1 = input ("Ingrese el primer valor: ")
var2 = input ("Ingrese el segundo valor: ")
var3 = input ("Ingrese el tercer valor: ")
prom = (var1 + var2 + var3) / 3
print "Los valores ingresados mayores al promedio son: "
if prom < var1:
	print "el valor: ", var1
if prom < var2:
	print "el valor: ", var2
if prom < var3:
	print "el valor: ", var3
print " ----- "
print " ----- "
print "## Valores ascendentes ##"
var1 = input ("Ingrese el primer valor: ")
var2 = input ("Ingrese el segundo valor: ")
var3 = input ("Ingrese el tercer valor: ")
print " "
if var1 <= var2 and var1 <= var3:
	print "El primer valor es: ", var1
	if var2 <= var3:
		print "El segundo valor es: ", var2
		print "El tercer valor es: ", var3
	else:
		print "El segundo valor es: ", var3
		print "El tercer valor es ", var2
elif var2 <= var1 and var2 <= var3:
	print "El primer valor es: ", var2
	if var1 <= var3:
		print "El segundo valor es: ", var1
		print "El tercer valor es: ", var3
	else:
		print "El segundo valor es: ", var3
		print "El tercer valor es: ", var1
else:
	print "El primer valor es: ", var3
	if var1 <= var2:
		print "El segundo valor es: ", var1
		print "El tercer valor es: ", var2
	else:
		print "El segundo valor es: ", var2
		print "El tercer valor es ", var1
print " ----- "
print " ----- "
print "## AFIP Importe e Impuestos ##"
impor = input ("Ingrese el valor del importe a pagar: ")
imp_apli = input ("Ingrese el valor de los impuestos que van a aplicarse: ")
imporNeto = impor - imp_apli
if imporNeto != 0:
	if impor < imp_apli:
		print ("** ERROR 404 El impuesto supera al importe **")
	elif imporNeto > 0 and impor > 5000:
			print ("** Monto superado para consumidor final **")
	else:
		print "- El importe neto es de: ", imporNeto, " -"

else:
	print "** ERROR EL IMPORTE ES 0**"
print " ----- " #(><).
print " ----- "
print "## ANSES ##"
var_nac = input ("Ingrese su año de nacimiento: ")
ano_act = 2016
var_ant = input ("Ingrese los años de antiguedad en su trabajo: ")
if (ano_act - var_nac) < 60 and var_ant >= 25:
	print "Usted esta en condiciones de tramitar su JUBILACION POR ANTIGUEDAD JOVEN"
elif (ano_act - var_nac) >= 60 and var_ant < 25:
	print "Usted esta en condiciones de tramitar su JUBILACION POR EDAD"
elif (ano_act - var_nac) >= 60 and var_ant >= 25:
	print "Usted esta en condiciones de tramitar su JUBILACION POR ANTIGUEDAD ADULTA"
else:
	print "Usted no esta en condiciones de tramitar una JUBILACION"
print " ----- "
print " ----- "
print "## AÑOS BISIESTOS ##"
var_year = input ("Ingrese el anio al que desea calcular: ")
if (var_year % 400) == 0:
	print "El anio analizado es BISIESTO"
elif (var_year % 4) == 0 and (var_year % 100) != 0:
	print "El anio analizado es BISIESTO"
else:
	print "El anio analizado no es BISIESTO"
print " ----- "
print " ----- "
print "## AREAS DE TRIANGULOS Y CIRCULOS ##"
import math
valor_v = raw_input ("Desea calcular el area de un TRIANGULO (Y - N): ")
if valor_v == "Y" or valor_v == "y":
	base = input ("Ingrese la medida de la base del Triangulo: ")
	alt = input ("Ingrese la medida de la altura del Triangulo: ")
	print "El area del triangulo es de: ", (base * alt) / 2
else:
	valor_v = raw_input ("Desea calcular el area de un CIRCULO (Y - N): ")
	if valor_v == "Y" or valor_v == "y":
		rad = input ("Ingrese la medida del radio del Circulo: ")
		print "El area del circulo es de: ", round((math.pi * (rad ** 2)), 3)
	else:
		print "-- Gracias por utilizar MathPython --"
print " ----- "
print " ----- "
print "## EMPRESA ##"#(><).
nombre = raw_input ("Ingrese el nombre del Empleado: ")
print "Comprobando.. .. Correcto! existente en base de datos"
sueldo = input ("Ingrese el sueldo del empleado: ")
asis_mes = raw_input ("El empleado asistio el mes completo? (Y-N): ")
h_esp = input ("El empleado cumplio horas extra? especifique cuantas: ")
if h_esp <= 10: 
	if asis_mes == "Y" or asis_mes == "y":
		if h_esp >= 6 and h_esp <= 10:
			calc = 10.0/100
			print "--"
			print "El empleado deberia recibir un sueldo de ", ((sueldo * calc) + sueldo), " pesos."
		elif h_esp >= 3 and h_esp <= 5:
			calc = 3.0/100
			print "--"
			print "El empleado deberia recibir un sueldo de ", ((sueldo * calc) + sueldo), " pesos."
	else:
		if h_esp >= 3 and h_esp <= 10:
			calc = 2.0/100
			print "--"
			print "El empleado deberia recibir un sueldo de ", ((sueldo * calc) + sueldo), " pesos."
		else:
			print "El empleado deberia percibir su sueldo de ", sueldo, " sin adicionales."
else:
	print "ERROR 404. Las horas no pueden superar las 10 unidades en fines de semana"
print " ----- "
print " ----- "
