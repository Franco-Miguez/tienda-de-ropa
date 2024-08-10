
class ProductoCarrito():
    def __init__(
                    self, codigo : str , descripcion : str,
                    precio : float, cantidad : int, talle : str | None = None,
                    genero : str |  None = None, material : str | None = None,
                    descuento = 0
                ) -> None:
        """
        Args:
            descuento (int, optional): descuento es de 0 a 100 indica el %
        """
        self.codigo = codigo
        self.descricion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.talle = talle
        self.genero = genero
        self.material = material
        self.tipo_producto = "Ropa" if talle else "Accesorio"
        self.descuento = descuento
    
    def modificar_cantidad(self, cantidad : int):
        self.cantidad += cantidad
    
    def cambiar_precio(self, nuevo_precio : float):
        self.cambiar_precio = nuevo_precio
    
    def mostrar_total(self) -> float:
        resultado = self.precio*self.cantidad
        descuento = resultado * self.descuento / 100
        return resultado - descuento