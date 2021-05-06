# Author: Jacqueline Juarez Carrera
# Fecha: 23/abril/2021
#tablas.py

numero = input("Ingresa un numero: ")
num = int (numero)

if (num > 0):
  for i in range (1,11):
    print (num,"x",i,"=",num*i)
if (num <= 0):
    print ("ERROR, solo permite valores positivos")


