import csv
from productos.ropa import Ropa

class Importador():
    @classmethod
    def importar(cls, ruta : str):
        with open(ruta, newline="") as archivo:
            info = csv.DictReader(archivo)
            lista = []
            for linea in info:
                if "Talle" in linea.keys():
                    codigo = linea.get("Codigo")
                    talle = linea.get("Talle")
                    genero = linea.get("Genero")
                    precio = linea.get("Precio")
                    stock = linea.get("Stock")
                    descripcion = linea.get("Descripcion")
                    lista.append( Ropa(codigo, talle, genero, precio, stock, descripcion) )
            
            return lista
            

if __name__ == "__main__":
    for ropa in Importador.importar("ropa.csv"):
        print(ropa.get_info())