from importador import Importador

class Menu():
    def __init__(self) -> None:
        self.stock = Importador.importar("./csv/accesorios.csv")
        self.stock.extend(Importador.importar("./csv/ropa.csv"))
    
    def mostrar_menu(self):
        while True:
            print("\n\n\tMenu:")
            opcion = input("1. Vender\n2. Mostrar Stock\n3. Agregar Productos\n4. Salir\nOpcion: ")
            if opcion == "1":
                pass
            elif opcion == "2":
                for articulo in self.stock:
                    print(articulo.get_info())
                    
            elif opcion == "3":
                pass
            elif opcion == "4":
                quit()
            else:
                print("#"*10,"\n\tError la opcion que selecciono no esta disponible\n","#"*10, sep="")
    
    def mostrar_stock():
        pass

if __name__== "__main__":
    menu = Menu()
    menu.mostrar_menu()