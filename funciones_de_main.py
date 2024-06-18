#Aqui irán las funciones del programa.
#generar archivo json con los datos solicitados al ingresar trabajador.


def agregarTrabajadores():
    #Pedir datos
    
    import json

    flag = True
    flag1 = True
    flag2 = True
    flag3 = True

    while flag1:
        nombre = input("Agregue el nombre: ")
        if nombre == "":
            print("Este campo es obligatorio...")
        else:
            flag1 = False

    while flag2:
        apellido = input("Agregue el apellido: ")
        if apellido == "":
            print("Este campo es obligatorio...")
        else:
            flag2 = False

    while flag3:
        cargo = input("Agregue el cargo del trabajador: ")
        if cargo == "":
            print("Este campo es obligatorio...")
        else:
            flag3 = False

    while flag:
        try:
            sueldob = int(input("Agregue el sueldo bruto del trabajador: "))
            flag = False 
        except:
            print("El sueldo ingresado debe ser un número entero...")

    # Crear el nuevo trabajador
    nuevo_trabajador = {"nombre": nombre, "apellido": apellido, "cargo": cargo, "sueldob": sueldob}

    # Leer el archivo JSON existente
    try:
        with open("trabajadores.json", "r") as archivo:
            trabajadores = json.load(archivo)
    except:
        trabajadores = []

    # Agregar el nuevo trabajador a la lista
    trabajadores.append(nuevo_trabajador)

    # Guardar la lista actualizada en el archivo JSON
    with open("trabajadores.json", "w") as archivo:
        json.dump(trabajadores, archivo, indent=4)

    print(f"Trabajador {nombre} {apellido} agregado exitosamente.")



        

