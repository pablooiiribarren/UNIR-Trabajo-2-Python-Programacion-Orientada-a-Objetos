
# Crear una clase Producto con atributos para nombre(str), precio(float) y cantidad(int)
# Manejar excepciones para entradas inválidas (precios negativos, nombres vacíos, etc.)
class Producto:
    def __init__(self, nombre, precio, cantidad):
        try:
            self.nombre = str(nombre)
        except not nombre:
                raise ValueError("El nombre no puede estar vacío.")
        try:
            self.precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser un número.")
        try:
            self.cantidad = int(cantidad)
        except cantidad >= 0:
            raise ValueError("La cantidad no puede ser negativa.")
    
    # Implementar métodos para añadir, actualizar y mostrar información de productos
    def actualizar_producto(self, nuevo_precio):
        while nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = nuevo_precio
        return self.precio
    
    def actualizar_cantidad(self, nueva_cantidad):
        while nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = nueva_cantidad
        return self.cantidad
    
    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Valor Total: {self.calcular_valor_total()}"

 # Crea la clase Inventario con un constructor que inicialice una lista vacía para almacenar productos  
class Inventario:
    def __init__(self):
        self.productos = []
    
    # Implementa métodos para añadir productos al inventario, eliminar productos por nombre y mostrar todos los productos
    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise ValueError("Solo se pueden agregar objetos de la clase Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None
    
    def calcular_valor_inventario(self):
        return sum(producto.calcular_valor_total() for producto in self.productos)
    
    def listar_productos(self):
        if not self.productos:
            return "El inventario está vacío."
        return "\n".join(str(producto) for producto in self.productos)
    
def main():
    inventario = Inventario()
    
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Mostrar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            try:
                nuevo_producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(nuevo_producto)
                print(f"Producto {nombre} agregado al inventario.")
            except ValueError as e:
                print(e)
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                try:
                    producto.actualizar_producto(nuevo_precio)
                    producto.actualizar_cantidad(nueva_cantidad)
                    print(f"Producto {nombre} actualizado.")
                except ValueError as e:
                    print(e)
            else:
                print(f"Producto {nombre} no encontrado en el inventario.")
        
        elif opcion == '3':
            print("\nProductos en el inventario:")
            print(inventario.listar_productos())
        
        elif opcion == '4':
            valor_total = inventario.calcular_valor_inventario()
            print(f"Valor total del inventario: {valor_total}")
        
        elif opcion == '5':
            print("Saliendo del sistema de inventario.")
            break
        
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# En la sección principal del programa (bajo if __name__ == "__main__":), 
# instancia un objeto de la clase Inventario y llama a la función menu_principal() para iniciar la aplicación.
if __name__ == "__main__":
    main()
