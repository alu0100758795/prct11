from info_ordenador import CPUinfo, SOinfo, InterpretePYinfo

if __name__=='__main__':
    nombre_fichero=raw_input("Introduzca el nombre deseado para el fichero")
    fichero=open(nombre_fichero, 'w')
    fichero.write("%s\n %s\n %s\n" %(CPUinfo(), SOinfo(), InterpretePYinfo()))
    fichero.close()