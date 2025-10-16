
# Crear una clase Producto con atributos para nombre(str), precio(float) y cantidad(int)
# Manejar excepciones para entradas inválidas (precios negativos, nombres vacíos, etc.)
import time
class Producto:
    def __init__(self, nombre, precio, cantidad):
        try:
            self.nombre = str(nombre)
        except ValueError:
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
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = nuevo_precio
        return self.precio
    
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = nueva_cantidad
        return self.cantidad
    
    def calcular_valor_total(self):
        return self.precio * self.cantidad
    
    def __str__(self):
        return (f"Producto: {self.nombre} | " f"Precio: {self.precio:.2f} | " f"Cantidad: {self.cantidad} | " f"Valor Total: ${self.calcular_valor_total():.2f}")

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
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def calcular_valor_inventario(self):
        return sum(producto.calcular_valor_total() for producto in self.productos)
    
    def listar_productos(self):
        if not self.productos:
            return "El inventario está vacío."
        encabezado = "=== INVENTARIO DE PRODUCTOS ==="
        productos = "\n".join(str(producto) for producto in self.productos)
        return f"{encabezado}\n{productos}"
    
def menu_principal(inventario):
    # Función que muestra el menú y opera sobre la instancia de Inventario recibida
    while True:
        print("\n==== MENÚ DEL INVENTARIO ====")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Mostrar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            try:
                nombre = input("Ingrese el nombre del producto: ").strip()
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                nuevo_producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(nuevo_producto)
                print(f"Producto {nombre} agregado al inventario.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
            producto = inventario.buscar_producto(nombre)
            if producto:
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))  
                    producto.actualizar_producto(nuevo_precio)
                    producto.actualizar_cantidad(nueva_cantidad)
                    print(f"Producto {nombre} actualizado correctamente.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"Producto {nombre} no encontrado en el inventario.")

        elif opcion == '3':
            print(inventario.listar_productos())

        elif opcion == '4':
            total = inventario.calcular_valor_inventario()
            print(f"Valor total del inventario: ${total:.2f}")

        elif opcion == '5':
            print("Saliendo del sistema de inventario...")
            time.sleep(3)
            break

        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# En la sección principal del programa (bajo if __name__ == "__main__":), 
# instancia un objeto de la clase Inventario y llama a la función menu_principal() para iniciar la aplicación.
if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
