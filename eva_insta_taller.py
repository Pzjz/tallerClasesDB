from baseDatos import *
import tkinter as tk
from tkinter import messagebox

connection = connect("localhost","root","","taller1")
cursor = connection.cursor()

crearAlmacenadoUser = """CREATE PROCEDURE alamcena_user (usuario VARCHAR(50),contraseña INT)
INSERT INTO login(usuario,contraseña) VALUES (usuario,contraseña)"""

class User:
    def insertUser(self, username,password):
        run_alamacena = "CALL alamcena_user (%s, %s)"
        values = (username,password)
        cursor.execute(run_alamacena,values)
    
    def userLogin(self,username,password):
        self.user = username
        cursor.execute("SELECT usuario,contraseña FROM login WHERE usuario=%s AND contraseña=%s",(username,password)) 
        resultadoLogin = cursor.fetchone()
        if resultadoLogin:
            mostrar_ventana2()
        else:
            mostrar_error()
            
    def insertar_monto(self,monto):
        valor = monto
        us = self.user
        cursor.execute("SELECT id FROM login WHERE usuario = %s",(us,))
        result = cursor.fetchone()
        id = result[0]
        insert = "UPDATE cuenta SET saldo = saldo + %s WHERE id = %s"
        values=(valor,id)
        cursor.execute(insert,values)

    def retirar_monto(self,monto):
        valor = monto
        us = self.user
        cursor.execute("SELECT id FROM login WHERE usuario = %s",(us,))
        result = cursor.fetchone()
        id = result[0]
        insert = "UPDATE cuenta SET saldo = saldo - %s WHERE id = %s"
        values=(valor,id)
        cursor.execute(insert,values)


user = User()


def mostrar_ventana1():
    ventana2.withdraw()
    ventana3.withdraw()
    ventana1.deiconify()
    
def mostrar_ventana2():
    ventana1.withdraw()
    ventana3.withdraw()
    ventana2.deiconify()

def mostrar_ventana3():
    ventana1.withdraw()
    ventana2.withdraw()
    ventana3.deiconify()    


def consulta_login():
    usuario = entryUser.get()
    contra = entryContra.get()
    user.userLogin(usuario,contra)

def retiro_dinero():
    retiro = entryValor.get()
    user.retirar_monto(retiro)
    connection.commit()

def consignacion_cuenta():
    consignar = entryValorC.get()
    user.insertar_monto(consignar)
    connection.commit()

def registrase_cuenta():
    nombre = entryValorUser.get()
    contraseña = entryValorContra.get()
    user.insertUser(nombre,contraseña)
    connection.commit()
    mostrar_error1()
    ventana3.destroy()


def mostrar_error():
    ventana1 = messagebox.showinfo("ERROR","Error datos invalidos (Noconexion)")

def mostrar_error1():
    ventana3 = messagebox.showinfo("Satisfactorio","Registro valido, de 1 a 6 dias se enviara un correo con el numero de cuenta ")


def mostrar_label():
    if etiqueta.winfo_ismapped():
        etiqueta.place_forget()
        entryValor.winfo_ismapped()
        entryValor.place_forget()
        botonEjecutar.winfo_ismapped()
        botonEjecutar.place_forget()
    else: 
        etiqueta.place(x=10,y=10,width=200,height=30)
        entryValor.place(x=220,y=10,width=200,height=30)
        botonEjecutar.place(x=220,y=50,width=200,height=30)

ventana1 = tk.Tk()
ventana1.geometry("300x300")
ventana1.title("Cajero")
ventana1.configure(bg="#959595")
lbUsuario = tk.Label(ventana1,text="Usuario",bg="#456F47")
lbUsuario.place(x=10,y=55,width=100,height=30)
lbContraseña = tk.Label(ventana1,text="Contraseña",bg="#456F47")
lbContraseña.place(x=10,y=100,width=100,height=30)
entryUser = tk.Entry(ventana1) 
entryUser.place(x=120,y=55,width=150,height=29)
entryContra = tk.Entry(ventana1)
entryContra.place(x=120,y=100,width=150,height=29)
boton = tk.Button(ventana1,text="Ingresa",command=consulta_login,cursor="right_ptr")
boton.place(x=120,y=150,width=150,height=29)
botonR = tk.Button(ventana1,text="Registrarse",cursor="right_ptr",command=mostrar_ventana3)
botonR.place(x=120,y=190,width=150,height=29)

ventana2 = tk.Toplevel()
ventana2.geometry("500x700")
ventana2.title("Transaccion")
ventana2.configure(bg="#959595")
entryValorC = tk.Entry(ventana2) 
entryValorC.place(x=220,y=10,width=200,height=30)
entryValor = tk.Entry(ventana2) 
entryValor.place(x=220,y=10,width=200,height=30)
etiquetaC = tk.Label(ventana2,text="Consignacion",background="#456F47",fg="white")
etiquetaC.place(x=10,y=10,width=200,height=30)
etiqueta = tk.Label(ventana2,text="Retiro de cuenta",background="#456F47",fg="white")
etiqueta.place(x=10,y=10,width=200,height=30)
botonCambiar = tk.Button(ventana2,text="Cambiar la transaccion",command=mostrar_label)
botonCambiar.place(x=10,y=50,width=200,height=30)
botonEjecutarC = tk.Button(ventana2,text="Consignar",command=consignacion_cuenta)
botonEjecutarC.place(x=220,y=50,width=200,height=30)
botonEjecutar = tk.Button(ventana2,text="Retirar",command=retiro_dinero)
botonEjecutar.place(x=220,y=50,width=200,height=30)

ventana3 = tk.Toplevel()
ventana3.geometry("500x700")
ventana3.title("Registro")
ventana3.configure(bg="#959595")
etiquetaUser = tk.Label(ventana3,text="Ingresar usuario",background="#456F47",fg="white")
etiquetaUser.place(x=10,y=10,width=150,height=30)
etiquetaContra = tk.Label(ventana3,text="Ingresar Contraseña",background="#456F47",fg="white")
etiquetaContra.place(x=10,y=50,width=150,height=30)
entryValorUser = tk.Entry(ventana3) 
entryValorUser.place(x=180,y=10,width=200,height=30)
entryValorContra = tk.Entry(ventana3) 
entryValorContra.place(x=180,y=50,width=200,height=30)
botonEjecutarC = tk.Button(ventana3,text="Registro",command=registrase_cuenta)
botonEjecutarC.place(x=180,y=100,width=200,height=30)


mostrar_ventana1()

ventana1.mainloop()

connection.commit()
connection.close()