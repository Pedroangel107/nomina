#la "a" anexa informacion y la "w" elimina o sobreescribe, la "r" sirve para leer, la "x" para crear archivo
#para cambiar un formato texto a numero se debe colocar ('numero=% s' %numero)
#para crear un archivo se utiliza la siguiente operacion:
#file = open('almacenamiento.txt','x')
#file.close()
n=int(input('Cuantos registros va incluir: '))
registros=[]
for i in range(n):
  registros.append(n)
  codigo=int(input('Codigo: '))
  nombre=(input('Nombre del empleado: '))
  apellido=(input('Apellido del empleado: '))
  cedula=int(input('Numero de cedula: '))
  dias_trabajados=int(input('Dias trabajados: '))
  sueldo_minimo=1160000
  transporte=200000
  sueldo_devengado=(sueldo_minimo//30*dias_trabajados)
  auxilio_transporte=(140606//30*dias_trabajados)
  descuento_salud=sueldo_devengado*4//100
  descuento_pension=sueldo_devengado*4//100
  total_pagar=(sueldo_devengado+auxilio_transporte)-(descuento_pension+descuento_salud)
  almacenar=open("almacenamiento.txt","a")
  almacenar.write('\n')
  almacenar.write('% s' %codigo+' ')
  almacenar.write(nombre+' ')
  almacenar.write(apellido+' ')
  almacenar.write('% s'%cedula+' ')
  almacenar.write('% s'%dias_trabajados+' ')
  almacenar.write('% s'%sueldo_devengado+' ')
  almacenar.write('% s'%descuento_salud+' ')
  almacenar.write('% s'%descuento_salud+' ')
  almacenar.write('% s'%total_pagar)

  print('-------DESPRENDIBLE DE PAGO--------')
  print('Nombre____________________',nombre)
  print('Apellido__________________',apellido)
  print('Cedula____________________',cedula)
  print('Dias trabajados___________',dias_trabajados)
  print('_________')
  print('Total devengado')
  print('Sueldo devengado__________',sueldo_devengado)
  print('Auxilio de transporte_____',auxilio_transporte)
  print('_________________')
  print('Total deducciones')
  print('Aporte a Salud____________',descuento_salud)
  print('Aporte a pension__________',descuento_pension)
  print('________________')
  print('Total a pagar_____________',total_pagar)
  print('\n')
  almacenar.close()  
print('has terminado de llenar los registros')