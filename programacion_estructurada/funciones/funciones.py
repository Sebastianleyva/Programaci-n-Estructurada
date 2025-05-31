"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#   1.- Funcion que no recibe parametros y no regresa valor
def solicitar_datos1():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    print(f"El nombre es: {nombre} y su telefono es: {telefono}")

#   3.- Funcion que recibe parametros y no regresa valor
def solicitar_datos3(nom,tel):
    nombre=nom
    telefono=tel
    print(f"El nombre es: {nombre} y su telefono es: {telefono}")

#   2.- Funcion que no recibe parametros y regresa valor
def solicitar_datos2():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    return nombre,telefono
#   4.- Funcion que recibe parametros y regresa valor
def solicitar_datos4(nom,tel):
    nombre=nom
    telefono=tel
    return nombre,telefono

#invocar funciones 

solicitar_datos1()

nombre,telefono=solicitar_datos2()
print(f"Agenda telefonica: \t nombre: {nombre} \t telefono: {telefono}")

nomre=input("Nombre")
telefono=input("Telefono")
solicitar_datos3(nombre,telefono)

nomre=input("Nombre")
telefono=input("Telefono")
nombre,telefono=solicitar_datos4(nombre,telefono)
print(f"Agenda felefonica \t nombre: {nombre} \t telefono: {telefono}")

