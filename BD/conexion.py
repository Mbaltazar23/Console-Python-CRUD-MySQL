import mysql.connector
from mysql.connector import Error


class DAO():  # DAO => Data Access Object
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='1234',
                db='bd_video'
            )
        except Error as ex:
            print("Error al intentar conectar la BD: {0}".format(ex))

    def listarProducts(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM producto ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar conectar la BD: {0}".format(ex))

    def registrarProducto(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO producto(nombre,precio,stock) VALUES('{0}','{1}',{2}) "
                cursor.execute(sql.format(
                    producto[0], producto[1], producto[2]))
                self.conexion.commit()
                print(" Producto registrado !! \n")
            except Error as ex:
                print("Error al intentar conectar la BD: {0}".format(ex))

    def actualizarProducto(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE producto SET nombre = '{0}', precio = {1}, stock= {2} WHERE codigo = {3}"
                cursor.execute(sql.format(
                    producto[1], producto[2], producto[3], producto[0]))
                self.conexion.commit()
                print(" Producto actualizado !! \n")
            except Error as ex:
                print("Error al intentar conectar la BD: {0}".format(ex))


    def eliminarProducto(self, codigoProducto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM producto WHERE codigo = {0}"
                cursor.execute(sql.format(codigoProducto))
                self.conexion.commit()
                print(" Producto Eliminado !! \n")
            except Error as ex:
                print("Error al intentar conectar la BD: {0}".format(ex))