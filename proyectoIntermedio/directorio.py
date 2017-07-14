#Programa de un directorio de contactos#
#Utilizando los módulos de tkinter     #
# sqlite3 y re                         #
#Realizado por: DLRSF                  #
#Como proyecto intermedio curso PROTECO#

#-*- coding: utf-8 -*-#
from tkinter import *
from tkinter import messagebox
import re
import sqlite3

def limpia():
    list = v.pack_slaves()
    for l in list:
        l.destroy()
def muestra():
    conexion=sqlite3.connect(r"agenda.sqlite")
    consulta=conexion.cursor()
    sql="SELECT * FROM contactos"
    if consulta.execute(sql):
        filas=consulta.fetchall()
        lbl=Label(v,text="Nombre\tCorreo\tNum.telefónico\tNum.cel").pack()
        for fila in filas:
            lb=Label(v,text=fila[1]+"  "+fila[2]+"  "+str(fila[3])+"  "+str(fila[4])).pack()
    consulta.close()
    conexion.commit()
    conexion.close()
def inicio():
    limpia()
    lb=Label(v,text="Para vizualiar sus contactos haga click en el botón").pack()
    bt=Button(v,text="Mostrar conotactos",command=muestra).pack()
def valida():
    nombre=et1.get()
    patron='^[(a-z0-9\_\.\-)]+@[(a-z0-9\_\.\-)]+\.[(a-z)]{2,3}$'
    correo=et2.get()
    ntel=et3.get()
    ctel=et4.get()
    if re.match("\D",nombre):
        #lb=Label(v,text=nombre).pack()
        if re.match(patron,correo):
            #lb=Label(v,text=correo).pack()
            if re.match("\d{8}",ntel):
                #lb=Label(v,text=ntel).pack()
                if re.match("55\d{8}",ctel):
                    #lb=Label(v,text=ctel).pack()
                    #guardando info en la base de datos
                    # addBD()
                    return True
                else:
                    messagebox.showinfo("Error","Por favor ingresa el número celular de forma correcta")
            else:
                messagebox.showinfo("Error","Por favor ingresa el número telefónico de forma correcta")
        else:
            messagebox.showinfo("Error","Por favor ingresa el correo de forma correcta")
    else:
        messagebox.showinfo("Error","Por favor ingresa el nombre de forma correcta")
def add():
    creaBD()
    if busca()==False:
        if valida()==True:
            addBD()
            messagebox.showinfo("Exito","Contacto creado")
    else:
        messagebox.showinfo("Error","El nombre del contacto ya existe")
def creaBD():
    conexion=sqlite3.connect(r"agenda.sqlite")
    consulta=conexion.cursor()
    sql="""
    CREATE TABLE IF NOT EXISTS contactos(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL,
    tel INTEGER NOT NULL,
    cel INTEGER NOT NULL
    )"""
    if consulta.execute(sql):
        pass#messagebox.showinfo("Exito","Directorio creado con exito")
    else:
        messagebox.showinfo("Error","No se puedo crear el directorio")
    consulta.close()
    conexion.commit()
    conexion.close()
def addBD():
    nombre=et1.get()
    correo=et2.get()
    tel=et3.get()
    cel=et4.get()
    conexion=sqlite3.connect(r"agenda.sqlite")
    consulta=conexion.cursor()
    datos=(nombre,correo,tel,cel)
    sql="""
    INSERT INTO contactos(nombre,correo,tel,cel)
    VALUES (?,?,?,?)
    """
    if consulta.execute(sql,datos):
        pass#messagebox.showinfo("Exito","Contacto creado")
    else:
        pass#messagebox.showinfo("Error","No se pudo crear contacto")
    consulta.close()
    conexion.commit()
    conexion.close()
def add_w():
    limpia()
    lb=Label(v,text="Por favor ingrese los datos solicitados del nuevo contacto").pack()
    lb1=Label(v,text="Nombre:").pack()
    global et1
    et1=Entry(v,bd=5)
    et1.pack()
    lb2=Label(v,text="Correo electrónico").pack()
    global et2
    et2=Entry(v,bd=5)
    et2.pack()
    lb3=Label(v,text="Número teléfonico").pack()
    global et3
    et3=Entry(v,bd=5)
    et3.pack()
    lb4=Label(v,text="Número de celular").pack()
    global et4
    et4=Entry(v,bd=5)
    et4.pack()
    bt=Button(v,text="Agregar contacto",command=add)
    bt.pack()
def busca():
    nombre=et1.get()
    conexion=sqlite3.connect(r"agenda.sqlite")
    consulta=conexion.cursor()
    diraux={}
    sql="SELECT * FROM contactos"
    if consulta.execute(sql):
        filas=consulta.fetchall()
        for fila in filas:
            diraux[fila[1]]=fila[0]
    if nombre in diraux:
        return True
    else:
        return False
    consulta.close()
    conexion.commit()
    conexion.close()
def up_w():
    limpia()
    lb=Label(v,text="Ingrese el nombre del contacto que desea actualizar").pack()
    lb1=Label(v,text="Nombre:").pack()
    global et1
    et1=Entry(v,bd=5)
    et1.pack()
    bt=Button(v,text="Buscar contacto",command=up)
    bt.pack()
def up():
    nombre=et1.get()
    if busca()==True:
        l=Label(v,text="Porfavor complete los datos")
        lb2=Label(v,text="Correo electrónico").pack()
        global et2
        et2=Entry(v,bd=5)
        et2.pack()
        lb3=Label(v,text="Número teléfonico").pack()
        global et3
        et3=Entry(v,bd=5)
        et3.pack()
        lb4=Label(v,text="Número de celular").pack()
        global et4
        et4=Entry(v,bd=5)
        et4.pack()
        bt=Button(v,text="Actualizar contacto",command=upBD)
        bt.pack()
    else:
        limpia()
        messagebox.showinfo("Error","Contacto no existe")
        up_w()
def upBD():
    if valida()==True:
        dellBD()
        addBD()
        messagebox.showinfo("Exito","Contacto actualizado")
    else:
        messagebox.showinfo("Error","No se pudo actualizar contacto")
def dellBD():
    nombre=et1.get()
    conexion=sqlite3.connect(r"agenda.sqlite")
    consulta=conexion.cursor()
    diraux={}
    sql="SELECT * FROM contactos"
    if consulta.execute(sql):
        filas=consulta.fetchall()
        for fila in filas:
            diraux[fila[1]]=fila[0]
    if nombre in diraux:
        x=diraux[nombre]
        sql="DELETE FROM contactos WHERE id=%s" %x
        if consulta.execute(sql):
            pass#contacto borrado
        else:
            pass#no se pudo borrar contacto
    else:
        pass#messagebox.showinfo("Error","Contacto no existe")
    consulta.close()
    conexion.commit()
    conexion.close()
def dell():
    if busca()==True:
        dellBD()
        messagebox.showinfo("Exito","Contacto borrado")
    else:
        messagebox.showinfo("Error","Contacto no existe")
def del_w():
    limpia()
    lb=Label(v,text="Ingrese el nombre del contacto que desea borrar").pack()
    lb1=Label(v,text="Nombre:").pack()
    global et1
    et1=Entry(v,bd=5)
    et1.pack()
    bt=Button(v,text="Buscar contacto",command=dell)
    bt.pack()

v=Tk()
v.geometry("450x250")
v.wm_title("Directorio")
menubar=Menu(v)

filemenu=Menu(menubar,tearoff=0)
menubar.add_command(label="Inicio",command=inicio)
menubar.add_command(label="Agregar contacto",command=add_w)
menubar.add_command(label="Modificar contacto",command=up_w)
menubar.add_command(label="Borrar contacto",command=del_w)
menubar.add_command(label="Salir",command=quit)

v.config(menu=menubar)
lb=Label(v,text="Para vizualiar sus contactos haga click en el botón").pack()
bt=Button(v,text="Mostrar conotactos",command=muestra).pack()
v.mainloop()
