from importador import Importador
from productos.ropa import Ropa
from productos.accesorio import Accesorio

class Menu():
    def __init__(self) -> None:
        self.stock = Importador.importar("./csv/accesorios.csv")
        self.stock.extend(Importador.importar("./csv/ropa.csv"))
    
    def mostrar_menu(self):
        while True:
            print("\n\n\tMenu:")
            opcion = input("1. Vender\n2. Mostrar Stock\n3. Agregar stock\n4. Salir\nOpcion: ")
            if opcion == "1":
                pass
            elif opcion == "2":
                self.mostrar_stock()
            elif opcion == "3":
                self.agregar_stock()
            elif opcion == "4":
                quit()
            else:
                print("#"*10,"\n\tError la opcion que selecciono no esta disponible\n","#"*10, sep="")
    
    def mostrar_stock(self):
        for articulo in self.stock:
            info = articulo.get_info()
            print(f"\n\t{info.get('Descripcion')}")
            print(f"Codigo: {info.get('Codigo')}")
            print(f"Stock: {info.get('Stock')}")
            print(f"Precio: {info.get('Precio')}")
            print(type(articulo) == type(Ropa("001","Xl", "Masculino")))
            if type(articulo) == type(Ropa("001","Xl", "Masculino")):
                print(f"Genero: {info.get("Genero")}")
                print(f"Talle: {info.get("Talle")}")
            else:
                print(f"Material: {info.get("Material")}")
    
    def agregar_stock(self):
        tipo = input("Ingrese que quiere agregar:\n1. Ropa\n2. Accesorio\nEleccion: ")
        nombre = input("Nombre: ")
        stock = input("Stock: ")
        precio = input("Precio: ")
        if tipo == "1":
            
            genero = input("1. Masculino\n2. Femenino\n3. unisex\nGenero: ")
            talle = input ("1. S\n2. M\n3. L\n4. XL\n Talles: ")
            
            if genero == "1": genero = "Masculino"
            elif genero == "2": genero = "Femenio"
            else: genero = "Unisex"
                
            if talle == "1": talle = "S"
            elif talle == "2": talle = "M"
            elif talle == "3": talle = "L"
            elif talle == "4": talle = "XL"
            
            Importador.exportar(nombre,stock,precio,genero,talle)
        else:
            material = input("Material: ")
            Importador.exportar(nombre, stock, precio, material=material)
        


if __name__== "__main__":
    menu = Menu()
    menu.mostrar_menu()