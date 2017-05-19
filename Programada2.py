import ast
import os.path
from tkinter import *
from tkinter import messagebox
from pathlib import Path

def cerrarVent(ventana):
    ventana.destroy()
    
def registrarCuenta():
    
    global contraseña
    global correo
    global CheckVar1

    save_path = "C:\\Python36\\TP2\\Usuarios"
    
    nombreArchivo = os.path.join(save_path, str(usuario.get()) + ".txt")

    archivo = open(nombreArchivo , "w+")
    archivo.close()

    contraseña = str(contraseña.get())
    correo = str(correo.get())
    esAdmin = CheckVar1.get()
    if esAdmin == 1:
        texto =  str(usuario.get()) + "\n" + contraseña + "\n" + correo + "\n" + "Tipo Cuenta: Admin"
    else:
        texto = str(usuario.get()) + "\n" + contraseña + "\n" + correo + "\n" + "Tipo Cuenta: Comprador" + "\n" + [] + "\n" + []
        
    archivo = open(nombreArchivo , "r+")
    archivo.write(texto)
    archivo.close()

    ventana_registro.destroy()
    
def ventana_inicioSesion():
    global usuarioIS
    global contraseñaIS
    def validarInicioSesion():
        global usuarioIS
        global contraseñaIS
        
        usuarioIS = str(usuarioIS.get())
        contraseñaIS = str(contraseñaIS.get())
        revisar = os.path.exists("C:\\Python36\\TP2\\Usuarios\\" + usuarioIS + ".txt")
        if revisar == True:
            archivoUsuario = open("C:\\Python36\\TP2\\Usuarios\\" + usuarioIS + ".txt")
            datosUsuario = archivoUsuario.readlines()
            contraseñaDato = datosUsuario[1]
            contraseñaDato = contraseñaDato.split("\n")[0]
            esAdminDato = datosUsuario[3]
            esAdminDato = esAdminDato.split("\n")[0]
            if contraseñaDato == contraseñaIS:
                if esAdminDato == "Tipo Cuenta: Admin":
                    ventanaInicioSesion.destroy()
                    return ventanaAdmin()
                else:
                    ventanaInicioSesion.destroy()
                    return ventanaComprador()
            else:
                messagebox.showerror("Error", "La contraseña no es correcta")
                ventanaInicioSesion.destroy()
            
        else:
            messagebox.showerror("Error", "Usuario no existe")
            
            ventanaInicioSesion.destroy()
        
    
    ventanaInicioSesion = Toplevel()

    usuarioIS = StringVar()
    labelUsuario = Label(ventanaInicioSesion, text = "Usuario: ").grid(row = 0,)
    ingresarUsuario = Entry(ventanaInicioSesion, textvariable = usuarioIS, width = 20)
    ingresarUsuario.grid(row = 0, column = 1)
    usuarioIS.get()

    contraseñaIS = StringVar()
    labelContraseña = Label(ventanaInicioSesion, text = "Contraseña: ").grid(row = 1)
    ingresarContraseña = Entry(ventanaInicioSesion, show = "*", textvariable = contraseñaIS, width = 20)
    ingresarContraseña.grid(row = 1, column = 1)
    contraseñaIS.get()

    boton = Button(ventanaInicioSesion, text = "Iniciar Sesion ", command = validarInicioSesion).grid(row = 2)

    cerrar = Button(ventanaInicioSesion, text = "Cerrar", command = lambda:cerrarVent(ventanaInicioSesion))
    cerrar.grid(row = 3, sticky = W)
    
    ventanaInicioSesion.mainloop()

def ventanaRegistro():
    global usuario
    global contraseña
    global correo
    global CheckVar1
    global ventana_registro
        
    ventana_registro = Toplevel()
    ventana_registro.geometry("700x300")

    usuario = StringVar()
    labelUsuario = Label(ventana_registro, text = "Usuario:").grid(row = 0, column = 0, sticky = W, pady = 5)
    crearUsuario = Entry(ventana_registro, textvariable=usuario, width = 30)
    crearUsuario.grid(row = 0, column = 1, pady = 5)

    contraseña=StringVar()
    labelContraseña = Label(ventana_registro, text = "Contraseña:").grid(row = 1, column = 0, sticky = W, pady = 5)
    crearContraseña = Entry(ventana_registro, textvariable = contraseña, show = "*", width = 30)
    crearContraseña.grid(row = 1, column = 1, pady = 5)

    correo = StringVar()
    labelCorreo = Label(ventana_registro, text = "Ingrese su correo:").grid(row = 3, column = 0, sticky = W, pady = 5)
    crearCorreo = Entry(ventana_registro, textvariable = correo, width = 30)
    crearCorreo.grid(row = 3, column = 1, pady = 5)

    CheckVar1 = IntVar()
    esAdmin = Checkbutton(ventana_registro, text = "Administrador", variable= CheckVar1, onvalue = 1, offvalue = 0)
    esAdmin.grid(row = 4)

    boton = Button(ventana_registro, text = "Registrar", command = registrarCuenta).grid(row = 5, sticky = W)

    cerrar = Button(ventana_registro, text = "Cerrar", command = lambda:cerrarVent(ventana_registro))
    cerrar.grid(row = 6, sticky = W)

    ventana_registro.mainloop()

def ventanaAdmin():
       
    def gestionProductos():
               
        def producto():        
            
            savepath = "C:\\Python36\\TP2\\Config"
            savepath = os.path.join(savepath, "Productos.txt")
            for productos in open(savepath, 'r'):
                listaProductos = ast.literal_eval(productos)

            listaProductos += [[nombreProducto.get(), precioProducto.get(), descripcionProducto.get(), categoriaProducto.get()]]

            archivo = open(savepath , "w+")
            archivo.seek(0 , 2)
            archivo.write(str(listaProductos))
            archivo.close()

            ventanaCrearProducto.destroy()
        def crearProducto():
            global nombreProducto
            global precioProducto
            global descripcionProducto
            global categoriaProducto
            global ventanaCrearProducto
            
            ventanaCrearProducto = Toplevel()
            nombreProducto = StringVar()
            labelnombreProducto = Label(ventanaCrearProducto, text = "Nombre Producto: ").grid(row = 0)
            entryNombreProducto = Entry(ventanaCrearProducto, textvariable = nombreProducto)
            entryNombreProducto.grid(row = 0, column = 1)
                
            precioProducto = StringVar()
            labelPrecioProducto = Label(ventanaCrearProducto, text = "Precio Producto: ").grid(row = 1)
            entryPrecioProducto = Entry(ventanaCrearProducto, textvariable = precioProducto)
            entryPrecioProducto.grid(row = 1, column = 1)
                
            descripcionProducto = StringVar()
            labelDescripcionProducto = Label(ventanaCrearProducto, text = "Descripcion Producto: ").grid(row = 2)
            entryDescripcionProducto = Entry(ventanaCrearProducto, textvariable = descripcionProducto)
            entryDescripcionProducto.grid(row = 2, column = 1)

            categoriaProducto = StringVar()
            labelCategoriaProducto = Label(ventanaCrearProducto, text = "Categoria Producto: ").grid(row = 3)
            entryCategoriaProducto = Entry(ventanaCrearProducto, textvariable = categoriaProducto)
            entryCategoriaProducto.grid(row = 3, column = 1)
                
            boton = Button(ventanaCrearProducto, text = "CREAR", command = producto)
            boton.grid(row = 4)
            
            ventanaCrearProducto.mainloop()
        return crearProducto()
    
    def gestionCategorias():
        def crearCategoria():
            global nombreCategoria
            
            ventanaCrearCat = Toplevel()

            nombreCategoria = StringVar()
            labelNombreCategoria = Label(ventanaCrearCat, text = "Nombre Categoría: ").grid(row = 0)
            entryNombreCategoria = Entry(ventanaCrearCat, textvariable = nombreCategoria)
            entryNombreCategoria.grid(row = 0, column = 1)
            
            botonCrearCategoria = Button(ventanaCrearCat, text = "CREAR", command = categoria).grid(row = 1)
            
            ventanaCrearCat.mainloop()
        def eliminarCategoria():
            ventanaEliminarCat = Toplevel()
            ventanaEliminarCat.mainloop()
        def modificarCategoria():
            ventanaModificarCat = Toplevel()
            ventanaModificarCat.mainloop()
        def categoria():
            global nombreCategoria
            savepath = "C:\\Python36\\TP2\\Config"
            savepath = os.path.join(savepath, "Categorias.txt")
            for categorias in open(savepath, 'r'):
                listaCategorias = ast.literal_eval(categorias)

            listaCategorias += [[nombreCategoria.get()]]

            archivo = open(savepath , "w+")
            archivo.seek(0 , 2)
            archivo.write(str(listaCategorias))
            archivo.close()
            
        ventanaGestionCategorias = Toplevel()

        botonCrearCat = Button(ventanaGestionCategorias, text = "Crear Categoría", command = crearCategoria).grid(row = 0)
        botonEliminarCat = Button(ventanaGestionCategorias, text = "Eliminar Categoría", command = eliminarCategoria).grid(row = 1)
        botonModificarCat = Button(ventanaGestionCategorias, text = "Modificar Categoría", command = modificarCategoria).grid(row = 2)
        
        ventanaGestionCategorias.mainloop()
    ventana_Admin = Toplevel()

    crearProducto = Button(ventana_Admin, text = "Gestion de Productos",command = gestionProductos)
    crearProducto.grid(row = 0)
    gestionProductos
    crearCategoria = Button(ventana_Admin, text = "Gestion de Categorías",command = gestionCategorias)
    crearCategoria.grid(row = 0, column = 1)
    
    ventana_Admin.mainloop()

def ventanaComprador():
    ventana_comprador = Toplevel()

    Label(ventana_comprador, text = "Ola K Ase x Aki?").grid(row = 0)

    ventana_comprador.mainloop()
    
ventanaPrincipal = Tk()

tsLabelTec = Label(ventanaPrincipal, text = "TEC", font = ("Arial",32), fg = "blue")
tsLabelTec.grid(row = 0)
tsLabelShop = Label(ventanaPrincipal, text = "SHOP", font = ("Arial",32))
tsLabelShop.grid(row = 0, column = 1)

iniciarSesion = Button(ventanaPrincipal, text = "Iniciar Sesión", command = ventana_inicioSesion)
iniciarSesion.grid(row = 1, sticky = W)

registrarse = Button(ventanaPrincipal, text = "Registrarse", command = ventanaRegistro)
registrarse.grid(row = 2, sticky = W)

ventanaPrincipal.mainloop()


