# la funcion del error

import sys, random
from math import *

def error(expr1, expr2, min_v, max_v, n_test, umbral):
  error=0
  i=0
  while i<n_test:
    a=random.uniform(min_v,max_v)
    b=random.uniform(min_v,max_v)
    if abs(eval(expr1)-eval(expr2))>umbral:
      error+=1
    i+=1
  porcentajeFallos=error*100/float(n_test)
  return porcentajeFallos

if __name__=='__main__':
  if len(sys.argv)==6:
    expr1=sys.argv[1]
    expr2=sys.argv[2]
    B=float(sys.argv[3])
    A=float(sys.argv[4])
    n=int(sys.argv[5])
    
    print "Porcentaje de fallos", error(expr1, expr2, A, B, n, umbral)
    
  else:
    print "el modo de uso es:%s expr1, expr2, valor minimo, valor maximo, numero de test" % (sys.argv[0])