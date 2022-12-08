def listarProducts(products):
    print("\nProductos: \n")
    contador = 1
    for pro in products:
        data = "{0}. Codigo : {1} | Nombre: {2} | Precio: {3} | Stock: {4}"
        print(data.format(contador, pro[0], pro[1], pro[2], pro[3]))
        contador = contador+1
    print(" ")


def pedirDatosInsertProduct():
    nombreCorrecto = False
    while (not nombreCorrecto):
        nombre = input("Ingrese el nombre :")
        if len(nombre) > 5:
            nombreCorrecto = True
        else:
            print("El nombre debe tener mas de 5 caracteres :(")

    precioCorrecto = False
    while (not precioCorrecto):
        precio = input("Ingrese el precio :")
        if precio.isnumeric():
            if int(precio) > 0:
                precioCorrecto = True
                precio = int(precio)
        else:
            print("El precio debe ser un entero :(")

    stockCorrect = False
    while (not stockCorrect):
        stock = input("Ingrese el stock :")
        if stock.isnumeric():
            if int(stock) > 0:
                stockCorrect = True
                stock = int(stock)
        else:
            print("El stock debe ser un entero :(")

    producto = (nombre, precio, stock)

    return producto


def pedirCodigoParaEliminar(productos):
    listarProducts(productos)
    existeCodigo = False
    codigoEliminar = int(input("Ingrese el codigo del producto a eliminar : "))
    for pro in productos:
        if pro[0] == codigoEliminar:
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar


def pedirDatosActualizarProducto(productos):
    listarProducts(productos)
    existeCodigo = False
    codigoEditar = int(input("Ingrese el codigo del producto a actualizar : "))
    for pro in productos:
        if pro[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombreCorrecto = False
        while (not nombreCorrecto):
            nombre = input("Ingrese el nombre a actualizar :")
            if len(nombre) > 5:
                nombreCorrecto = True
            else:
                print("El nombre debe tener mas de 5 caracteres :(")

        precioCorrecto = False
        while (not precioCorrecto):
            precio = input("Ingrese el precio a actualizar:")
            if precio.isnumeric():
                if int(precio) > 0:
                    precioCorrecto = True
                    precio = int(precio)
            else:
                print("El precio debe ser un entero :(")

        stockCorrect = False
        while (not stockCorrect):
            stock = input("Ingrese el stock a actualizar :")
            if stock.isnumeric():
                if int(stock) > 0:
                    stockCorrect = True
                    stock = int(stock)
            else:
                print("El stock debe ser un entero :(")

        producto = (codigoEditar, nombre, precio, stock)
    else:
        producto = None

    return producto
