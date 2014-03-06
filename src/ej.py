#!/usr/bien/python
#!enconding: UTF-8
import sys

def calcular_xi (n, i):
 xi = (i - 1.0/2.0) / n
 return xi
 
argumentos = sys.argv[1:] #desde la posicion uno hasta el final
print argumentos
if (len(argumentos) == 1):
   n = int (argumentos[0])
else:

   print "introduzca el numero de intervalos (n<0):"
   n = int (raw_input())
if (n>0):
   PI35 = 3.1415926535897931159979634685441852
   sumatorio = 0.0
   ini = 0
   intervalos = 1.0 / float (n)
   for i in range(n):
     x_i = ((i+1) - 1.0/2.0) / n
     fx_i = 4.0 / (1.0 + x_i * x_i)
     print "subintervalo: [", ini, ",", ini+intervalos,"] x_i:", x_i, " fx_i:", fx_i
     ini += intervalos
     sumatorio += fx_i
     valor_pi = sumatorio / n
   print "el valor aproximado de PI es:" , valor_pi
   print "el valor de PI con 35 decimales es : %10.35f" %PI35
else:
  print "el valor de los intervalos debe ser positivo"
    
    