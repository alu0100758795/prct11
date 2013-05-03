# uso de modulo_error
import sys, random, time
from math import *
from modulo_error import error

l=[('(a*b)**3','a**3*b**3'),('a/b','1/b/a'), ('exp(a+b)','exp(a)*exp(b)'), ('log(a**b)','b*log(a)'), ('a-b','-(b-a)'), ('(a*b)**4','a**4*b**4'), ('(a+b)**2','a**2+2*a*b+b**2'), ('(a+b)*(a-b)','a**2-b**2'), ('log(a*b)','log(a)+log(b)'),('a*b','exp(log(a)+log(b))'), ('1/(1/a+1/b)','(a*b)/(a+b)'), ('a*(sin(b)**2+cos(b)**2)','a'), ('sinh(a+b)','(exp(a)*exp(b)-exp(-a)*exp(-b))/2'), ('tan(a+b)','sin(a+b)/cos(a+b)'), ('sin(a+b)','sin(a)*cos(b)+sin(b)*cos(a)')]

u=[1.e-10, 1.e-50, 1.e-100, 1.e-150, 1.e-200]


if __name__=='__main__':
  
  if len(sys.argv)==5:
    B=float(sys.argv[1])
    A=float(sys.argv[2])
    n=int(sys.argv[3])
    nombre_fichero=sys.argv[4]
    fichero=open(nombre_fichero, 'w')
    
    e0 = time.time() # Unix epoch time
    c0 = time.clock() # CPU time
    
    for t in l:
      expr1=t[0]
      expr2=t[1]
      fichero.write("%s\n %s\n" %(expr1, expr2))
      for i in range(len(u)):
	fichero.write("%3.1f\n" %(error(expr1, expr2, A, B, n, u[i])))
	print "%s %s %3.1g" %(expr1, expr2, error(expr1, expr2, A, B, n, u[i]))
	i+=1
      fichero.write("Tarda en tiempo transcurrido: %s\n" %(time.time() - e0))
      fichero.write("Tarda en tiempo CPU:  %s\n" %(time.clock() - c0))
    fichero.close()
  else:
    print "el modo de uso es:%s valor minimo, valor maximo, numero de test, nombre fichero" % (sys.argv[0])