from tkinter import *
from tkinter import messagebox


def llamarVentana(ventana):
    ventana.deiconify()

def ocultarVentana(ventana):
    ventana.withdraw()

def crearArchivo():
    global usuario
    global contraseña
    global correo
    global CheckVar1
    
    
    nombreArchivo = usuario.get() + ".txt"

    archivo = open(nombreArchivo , "w+")
    archivo.close()

    contraseña = str(contraseña.get())
    correo = str(correo.get())
    esAdmin = str(CheckVar1.get())
        
    texto = "Contraseña:  " + crearContraseña + "\n" + "Correo: " + crearCorreo + "\n"
    
        
    archivo = open(nombreArchivo , "r+")
    archivo.write(texto)
    archivo.close()
    if esAdmin == 1:
        return crearCuentaAdmin()
    else:
        return crearCuentaUsuario()
    
        
def crearCuentaAdmin():
    global crearUsuario
    global listaCategorias
    global listaProductos
    
    nombreUsuario = crearUsuario.get() + ".txt"

    texto = "Administrador = Sí" + "\n" 
    
    archivo = open(nombreUsuario , "r+")
    archivo.seek(0 , 2)
    archivo.write(texto)
    
    archivo.close()
      
def crearCuentaUsuario():
    global crearUsuario
    

##VENTANAS##
ventanaPrincipal = Tk()
ventana_inicioSesion = Toplevel(ventanaPrincipal)
ventana_registro = Toplevel(ventanaPrincipal)


iniciarSesion = Button(ventanaPrincipal, text = "Iniciar Sesión", command = lambda:llamarVentana(ventana_inicioSesion))
iniciarSesion.grid(row = 0)

registrarse = Button(ventanaPrincipal, text = "Registrarse", command = lambda:llamarVentana(ventana_registro))
registrarse.grid(row = 1)
##----------------------------##


##VENTANA INICIO SESIÓN##

labelUsuario = Label(ventana_inicioSesion, text = "Usuario").grid(row = 0, column = 0)
ingresarUsuario = Entry(ventana_inicioSesion)
ingresarUsuario.grid(row = 0, column = 1)

labelContraseña = Label(ventana_inicioSesion, text = "Contraseña").grid(row = 1, column = 0)
ingresarContraseña = Entry(ventana_inicioSesion, show = "*")
ingresarContraseña.grid(row = 1, column = 1)

boton = Button(ventana_inicioSesion, text = "Iniciar Sesion ").grid(row = 2)

cerrar = Button(ventana_inicioSesion, text = "Cerrar", command = lambda:ocultarVentana(ventana_inicioSesion))
cerrar.grid(row = 3)
##----------------------------##


##VENTANA REGISTRO##
usuario = StringVar()
labelUsuario = Label(ventana_registro, text = "Usuario:").grid(row = 0, column = 0, sticky = W)
crearUsuario = Entry(ventana_registro)
crearUsuario.grid(row = 0, column = 1)

contraseña = StringVar()
labelContraseña = Label(ventana_registro, text = "Contraseña:").grid(row = 1, column = 0, sticky = W)
crearContraseña = Entry(ventana_registro, textvariable=contraseña, show = "*")
crearContraseña.grid(row = 1, column = 1)

correo = StringVar()
labelCorreo = Label(ventana_registro, text = "Ingrese su correo:").grid(row = 3, column = 0, sticky = W)
crearCorreo = Entry(ventana_registro, textvariable=correo)
crearCorreo.grid(row = 3, column = 1)

CheckVar1 = IntVar()
esAdmin = Checkbutton(ventana_registro, text = "Administrador", variable= CheckVar1, onvalue = 1, offvalue = 0)
esAdmin.grid(row = 4)

boton = Button(ventana_registro, text = "Registrar", command = crearArchivo).grid(row = 5, sticky = W)

cerrar = Button(ventana_registro, text = "Cerrar", command = lambda:ocultarVentana(ventana_registro))
cerrar.grid(row = 6, sticky = W)
##----------------------------##

##VARIABLES NECESARIAS PARA GESTIÓN##

    #Admin#
listaCategorias = []
listaProductos = []
listaVentas = []

    #Comprador#
listaDeseos = []
carrito = []
listaCompras = []
##----------------------------##

##MANEJO DE ERRORES##
#ventana_registro.protocol("WM_DELETE_WINDOW", "onexit")
#ventana_inicioSesion.protocol("WM_DELETE_WINDOW", "onexit")
##----------------------------##


##FUNCIONAMIENTO DE VENTANAS##
ventana_inicioSesion.withdraw()
ventana_registro.withdraw()
ventanaPrincipal.mainloop()
##----------------------------##
