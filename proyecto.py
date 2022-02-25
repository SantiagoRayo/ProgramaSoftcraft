# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:17:15 2021

@author: RAYO
"""
import pandas as pd

lista = list()
lista2 = list()
lista3 = list()



class artesanos:
    def __init__(self):
        self.nombre =()
        self.edad =()
        self.telefono =()
        self.correo =()
        self.documento = ()
        self.ID = ()
      
class contador(object):

  def __init__(self, c=1):
    self.num = c

  def Siguiente(self):
    self.num += 1
    return self.num    

contar = contador()
      
        
class clientes:
    def __init__(self):
        self.nombre = ()
        self.edad = ()
        self.telefono = ()
        self.correo = ()
        self.documento = ()
        self.ID = ()

class Contar(object):

  def __init__(self, c=1):
    self.Numero = c

  def siguient(self):
    self.Numero += 1
    return self.numero    

c = Contar()


class productos:
    def __init__(self):
        self.nombre = ()
        self.codigo = ()
        self.descripcion = ()
        self.precio = ()
        self.ID = ()
        
class Contador(object):

  def __init__(self, c=1):
    self.numero = c

  def siguiente(self):
    self.numero += 1
    return self.numero    

contador = Contador()

def menu():
    seleccion = 0
    while seleccion != 8:
        print("###################################################################")
        print("Programa de softcraft")
        print("###################################################################")
        print("1. Registro de Artesanos")
        print("2. Registro de Clientes")
        print("3. Registro de Productos")
        print("4. Compra de Productos")
        print("5. Consultar Artesanos")
        print("6. Consultar Clientes")
        print("7. Consultar Prodcutos")
        print("8. Salir")
        seleccion =int(input("Por favor seleccione una opcion del menu: "))
        
    
        if seleccion == 1:
            registrar1()
          
            
        if seleccion == 2:
            registrar2()
    
    
        if seleccion == 3:
            registrar3()
    
    
        if seleccion == 4:
            comprar()
            
        if seleccion == 5:
            mostrar1()
            
        if seleccion == 6:
            mostrar2()
            
        if seleccion == 7:
            mostrar3()
            
        if seleccion == 8:
            salir()


def registrar1():
    print("Este es el Registro de los Artesanos")
    artesano = artesanos()
    artesano.nombre=input("Introduzca su nombre: ")
    artesano.edad=int(input("Introduzca su edad: "))
    artesano.correo=input("Introduzca su correo electronico: ")
    artesano.telefono=int(input("Introduzca su telefono: "))
    artesano.documento=int(input("Introduzca su numero de identificacion: "))
    
    artesano.ID = contar.num
    contar.Siguiente()
    lista.append(artesano)



    
def registrar2():
    print("Este es el Registro de los Clientes")
    cliente = clientes()
    cliente.nombre=input("Introduzca su nombre: ")
    cliente.edad=int(input("Introduzca su edad: "))
    cliente.correo=input("Introduzca su correo electronico: ")
    cliente.telefono=int(input("Introduzca su telefono: "))
    cliente.documento=int(input("Introduzca su numero de identificacion: "))
    
    cliente.ID = c.Numero
    c.siguient()
    lista2.append(cliente)



def registrar3():
    print("Este es el registro de los Producos")
    producto = productos()
    producto.nombre=input("Introduzca el nombre del producto: ")
    producto.codigo=input("Introduzca el codigo del producto: ")
    producto.precio=input("Introduzca el precio del producto: ")
    producto.descripcion=input("Introduzca una descripcion del producto: ")
    
    producto.ID = contador.numero
    contador.siguiente()
    lista3.append(producto)


    
def mostrar1():
    print("Registro de los artesanos \n")
    for artesano in lista:
        print(artesano.ID,"-","el nombre del artesano es: ",artesano.nombre,
              " la edad del artesano es: ",artesano.edad,
              " el telefono del artesano es: ",artesano.telefono,
              " el correo del artesano es: ",artesano.correo,
              " el documento de identificacion del artesano es: ",
              artesano.documento, "\n")
        
     
def mostrar2():
    print("Registro de los clientes \n")
    for cliente in lista2:
        print(cliente.ID,"-","el nombre del clientes es: ",cliente.nombre,
        "la edad del cliente es: ",cliente.edad,
        "el telefono del cliente es: ",cliente.telefono,
        "el correo del cliente es: ",cliente.correo,
        "el documento de identificacion del cliente es: ",cliente.documento,"\n")
        
def mostrar3():
    
    print("Registro de productos \n")
    for producto in lista3:
        print(producto.ID,"-","el nombre del producto es: ",producto.nombre,
        "el codigo del pruducto es: ",producto.codigo,
        "precio delproducto es: ",producto.precio,
        "la descripcion del producto es: ",producto.descripcion,"\n")
        
        
def comprar():
    numProducto = 0
    print("#################################################################")
    print("Compra de Productos")
    print("#################################################################")
    for producto in lista3:
        print(producto.ID,"-","Nombre:",producto.nombre," Precio $",producto.precio)
        
    numProducto = int(input("Eliga el numero del producto que desea comprar: "))


    if any(producto.ID == numProducto for producto in lista3):
        print("Gracias por su compra")
       
            
    else:
        print("Ese producto no existe")
     

def salir():
    print("Gracias por usar este programa vuelva pronto")
    
  
menu() 
