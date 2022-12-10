from BD.conexion import DAO
import functions.funciones as funciones


def menuPrincipal():
    continuar = True
    while (continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print("========= Menu Principal ========")
            print("    1- Listar Productos")
            print("    2- Registrar Producto")
            print("    3- Actualizar Producto")
            print("    4- Eliminar Producto")
            print("    5- Salir")
            print("=================================")

            opcion = int(input("Seleccione una opcion : "))

            if opcion < 1 or opcion > 5:
                print("Opcion incorrecta, intente nuevamente... :(")
            elif opcion == 5:
                continuar = False
                print("Gracias por probar el programa :)")
                break  # con esto cortamos el bucle del while
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        print("Opcion 1 procesada")
        try:
            products = dao.listarProducts()
            if len(products) > 0:
                # hacer algo
                funciones.listarProducts(products)
            else:
                print("No hay productos registrados")
        except:
            print("Ocurrio un error :(")

    elif opcion == 2:
        print("Opcion 2 procesada")
        producto = funciones.pedirDatosInsertProduct()
        try:
            dao.registrarProducto(producto)
        except:
            print("Ocurrio un error al registrar :(")

    elif opcion == 3:
        print("Opcion 3 procesada")
        try:
            products = dao.listarProducts()
            if len(products) > 0:
                producto = funciones.pedirDatosActualizarProducto(products)
                if producto:
                    dao.actualizarProducto(producto)
                else:
                    print("Codigo del producto no encontrado .. :( \n")
            else:
                print("No se encuentra ningun producto :(")
        except:
            print("Ocurrio un error al eliminar :(")

    elif opcion == 4:
        print("Opcion 4 procesada")
        try:
            products = dao.listarProducts()
            if len(products) > 0:
                codigo = funciones.pedirCodigoParaEliminar(products)
                if not (codigo == ""):
                    dao.eliminarProducto(codigo)
                else:
                    print("Codigo de producto no encontrado :(")
            else:
                print("No se encuentra ningun producto :(")
        except:
            print("Ocurrio un error al eliminar :(")


menuPrincipal()
