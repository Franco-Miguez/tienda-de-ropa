import csv
from productos.ropa import Ropa
from productos.accesorio import Accesorio

class Importador():
    @classmethod
    def importar(cls, ruta : str):
        with open(ruta, newline="") as archivo:
            info = csv.DictReader(archivo)
            lista = []
            for linea in info:
                codigo = linea.get("Codigo")
                precio = linea.get("Precio")
                stock = linea.get("Stock")
                descripcion = linea.get("Descripcion")
                if "Talle" in linea.keys():
                    talle = linea.get("Talle")
                    genero = linea.get("Genero")
                    lista.append( Ropa(codigo, talle, genero, precio, stock, descripcion) )
                elif "Material" in linea.keys():
                    material = linea.get("Material")
                    lista.append( Accesorio(codigo, material, precio, stock, descripcion) )
            return lista
            

if __name__ == "__main__":
    productos = Importador.importar("ropa.csv")
    productos.extend(Importador.importar("accesorios.csv"))
    for producto in productos:
        print(producto.get_info())