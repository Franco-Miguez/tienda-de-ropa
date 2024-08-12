import csv
from productos.ropa import Ropa
from productos.accesorio import Accesorio

class Importador():
    @classmethod
    def importar(cls, ruta : str) -> list[object]:
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
            
    @classmethod
    def exportar(
                    cls, nombre : str, stock : int, precio : float,
                    genero : str | None = False, talle : str | None = False, material : str | None = False
                ):
        articulo = {}
        articulo["Codigo"] = cls.generar_codigo()
        articulo["Descripcion"] = nombre
        articulo["Stock"] = stock
        articulo["Precio"] = precio
        if talle: 
            ruta = "./csv/ropa.csv"
            articulo["Genero"] = genero
            articulo["Talle"] = talle
        else:
            ruta = "./csv/accesorios.csv"
            articulo["Material"] = material
        with open(ruta, mode="a") as archivo:
            titulos = ["Codigo","Precio","Stock","Descripcion"]
            if talle:
                titulos.insert(1,"Genero") 
                titulos.insert(1,"Talle") 
            else:
                titulos.insert(1,"Material")
                
            escribir = csv.DictWriter(archivo, titulos)
            
            escribir.writerow(articulo)
    
    @classmethod
    def generar_codigo(cls):
        with open("./csv/accesorios.csv") as archivo:
            info = csv.DictReader(archivo)
            for linea in info:
                codigo_accesorios = linea.get("Codigo")
        with open("./csv/ropa.csv") as archivo:
            info = csv.DictReader(archivo)
            for linea in info:
                codigo_ropa = linea.get("Codigo")
        if codigo_ropa > codigo_accesorios:
            return str(int(codigo_ropa) + 1)
        else:
            return str(int(codigo_accesorios) + 1)

if __name__ == "__main__":
    productos = Importador.importar("ropa.csv")
    productos.extend(Importador.importar("accesorios.csv"))
    for producto in productos:
        print(producto.get_info())