"""
1) Cargar producto
Solicitar código, nombre, precio y stock. Validar código no repetido, precio mayor a cero y
stock no negativo.
2) Mostrar productos
Mostrar todos los productos cargados de forma clara y ordenada.
3) Buscar producto por código
Buscar manualmente recorriendo la estructura de datos utilizada.
4) Ordenar productos por precio
Ordenar manualmente utilizando un algoritmo de ordenamiento.
5) Mostrar producto con menor stock
Determinar manualmente cuál es el producto con menor cantidad disponible.
6) Calcular valor total del inventario
Calcular el valor total del inventario considerando precio por stock.
"""
codigos = []
nombres = []
precios = []
cantidad = []

opcion = 0 

while opcion != "7":
    print("==============================\n"
        "SUPERMERCADO PYTHON MARKET\n"
        "==============================\n"
        "1. Cargar producto\n"
        "2. Mostrar productos\n"
        "3. Buscar producto por código\n"
        "4. Ordenar productos por precio\n"
        "5. Mostrar producto con menor stock\n"
        "6. Calcular valor total del inventario\n"
        "7. Salir\n"
    )
    int(input("Seleccione una opción para comenzar: "))
    
    
    match opcion: 
        
        case "1": #Agregar productos
            codigo = input(int("Ingrese el código de su producto: "))
            
            repetido = False 
            
            for i in range (len(codigos)):
                
                if codigos[i] == codigo:
                    repetido = True 
                
            if repetido == True: 
                print("El código ingresado ya existe.")
                
            else:
                nombre = input("Ingrese el nombre de su producto: ")
                
                precio = input(f"Ingrese el valor de su producto: ")
                
                while precio <= 0:
                    print("El precio debe ser mayor a $0")
                    precio = input(f"Ingrese nuevamente un valor: ")
                    
                cantidad_producto = int(input("Ingrese la cantidad del producto: "))
                
                while cantidad_producto < 0:
                    print("La cantidad del producto no puede ser menor a 0: ")
                    cantidad_producto =int(input("Ingrese nuevamente la cantidad del producto: "))
                    
                codigos.append(codigo)
                nombres.append(nombre)
                precios.append(precio)
                cantidad.append(cantidad_producto)
                
                print("El producto se ha cargado correctamente.")
                
                
                
        case "2": #Mostrar productos 
            
            if len(codigos) == 0:
                print("Aún no hay productos cargados.")
            
            else:
                print("\n____PRODUCTOS ACTUALMENTE DISPONIBLES____\n")  
                
                for i in range(len(codigos)): 
                    print("\nProducto", i + 1)
                    print("Código de producto: ", codigos[i])
                    print("Nombre de producto: ", nombres[i])
                    print("Código de producto: ", precios[i])
                    print("Cantidad disponible del producto", cantidad[i])
                    
                    
                    
        case "3": #Buscar productos
            
            buscar = int(input("Ingrese el código que desea buscar: "))      
            
            encontrado = False       
            
            for i in range(len(codigos)):
                
                if codigos[i] == buscar:
                    print("\nProducto encontrado")
                    print("Código de producto: ", codigos[i])
                    print("Nombre de producto: ", nombres[i])
                    print("Código de producto: ", precios[i])
                    print("Cantidad disponible del producto", cantidad[i])
                    
                    encontrado = True 
                    
            if encontrado == False: 
                print("Producto no encontrado.")
                
                
                
        case "4": #Ordenar productos por precio
            
            for i in range(len(precios))     
                
    
            
        case "5": #Mostrar producto con menor stock
            
