from productos.accesorio import Accesorio
from productos.ropa import Ropa
from producto_carrito import ProductoCarrito

class CarritoCompras():
    def __init__(self) -> None:
        self.carrito = []
    
    def agregar(self, producto : object):
        for articulo in self.carrito:           
            if articulo.get_info().get("Codigo") == producto.get_info().get("Codigo"):
                nuevo_valor =  articulo.get_info().get("Stock") + producto.get_info().get("Stock")
                indice = self.carrito.index(articulo)
                self.carrito[indice].set_stock(nuevo_valor) 
                return None
        self.carrito.append(producto)

    def mostrar(self):
        for producto in self.carrito:
            print(producto.get_info())
    
    def remover(self, codigo : str):
        for producto in self.carrito:
            if producto.get_info().get("Codigo") == codigo:
                self.carrito.remove(producto)
    
    def cantidad(self):
        return len(self.carrito)


if __name__ == "__main__":
    carrito = CarritoCompras()
    carrito.agregar(Ropa("001","XL","Masculino",stock=5))
    carrito.agregar(Ropa("001","XL","Masculino",stock=3))
    carrito.agregar(Ropa("002","XL","Masculino"))
    carrito.agregar(Ropa("003","XL","Masculino"))
    carrito.agregar(Ropa("004","XL","Masculino"))
    print(carrito.cantidad())
    carrito.mostrar()
    #print(carrito.cantidad())
    #carrito.mostrar()
