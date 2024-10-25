productos = []

def añadir_producto():
    # Lógica para añadir un producto
    nombre = input("Introduce el nombre del producto: ")
    try:
        precio = float(input("Introduce el precio del producto: "))
        cantidad = int(input("Introduce la cantidad disponible del producto: "))
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print(f"Producto '{nombre}' añadido correctamente.")
    except ValueError:
        print("Error: El precio debe ser un número decimal y la cantidad un número entero.")
    

def ver_productos():
    # Lógica para ver todos los productos
    cargar_datos()
    if productos:
        print("\nLista de productos:")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")
    else:
        print("No se cargaron productos en el inventario.")
    
    2

def actualizar_producto():
    # Lógica para actualizar un producto
    ver_productos()
    nombre = input("Introduce el nombre del producto que deseas actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            try:
                nuevo_nombre = input(f"Introduce el nuevo nombre (actual: {producto['nombre']}): ") or producto['nombre']
                nuevo_precio = input(f"Introduce el nuevo precio (actual: {producto['precio']}): ") or producto['precio']
                nueva_cantidad = input(f"Introduce la nueva cantidad (actual: {producto['cantidad']}): ") or producto['cantidad']
                producto['nombre'] = nuevo_nombre
                producto['precio'] = float(nuevo_precio)
                producto['cantidad'] = int(nueva_cantidad)
                print(f"Producto '{nombre}' actualizado correctamente.")
                return
            except ValueError:
                print("Error: El precio y la cantidad deben ser números.")
                return
    print(f"No se encontró un producto con el nombre '{nombre}'.")
    

def eliminar_producto():
    # Lógica para eliminar un producto
    ver_productos()
    nombre = input("Introduce el nombre del producto que deseas eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"No se encontró un producto con el nombre '{nombre}'.")  
    pass

def guardar_datos():
    try:
        with open("productos.txt", "w") as archivo:
            for producto in productos:
                archivo.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")
        print("Datos guardados exitosamente")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
        
def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(", ")
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró un archivo de datos existente.")
    

def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")
menu()