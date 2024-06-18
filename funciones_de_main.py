#Aqui irán las funciones del programa.
#generar archivo json con los datos solicitados al ingresar trabajador.


def agregarTrabajadores():
    #Pedir datos
    import time
    import json

    flag = True
    flag1 = True
    flag2 = True
    flag3 = True

    while flag1:
        print("\n\n")
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
        listaCargos=["CEO","Desarrollador","Analista de datos"]
        print("\n\n\nSeleccione su cargo en la empresa:\n")
        for i in range(len(listaCargos)):
            print(f"{i+1}. {listaCargos[i]}")
        try:
            cargo=int(input("Ingrese una opción--> "))
        except:
            print("Debe ingresar una opción númerica")
        else:
            if cargo>0 and cargo<4:
                flag3=False
                cargoN=listaCargos[cargo-1]
            else:
                print("Solo hay 3 opciones.")
    while flag:
        try:
            print("\n")
            sueldob = int(input("Agregue el sueldo bruto del trabajador: "))
            flag = False 
        except:
            print("El sueldo ingresado debe ser un número entero...")

    descuentoSalud=sueldob*0.07
    descuentoAFP=sueldob*0.12
    sueldoL=sueldob-descuentoAFP-descuentoSalud

    # Crear el nuevo trabajador
    nuevo_trabajador = {"nombre": nombre, "apellido": apellido, "cargo": cargoN, "sueldob": sueldob ,"descuentoSalud":descuentoSalud,"descuentoAFP":descuentoAFP,"sueldoL":sueldoL}

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

    print(f"\n\n\nTrabajador {nombre} {apellido} agregado exitosamente.")
    time.sleep(1);input("Presione ENTER para continuar...")



def listar_trabajadores():
    import json;
    import time;
    try:
        with open("trabajadores.json", "r") as archivo:
            trabajadores = json.load(archivo)
    except:
        print("No existen trabajadores.");
    else:
        for i in range(len(trabajadores)):
            print(f"Trabajador {i+1}:");
            trabajador=(trabajadores[i]);
            print(f"Nombre: {trabajador["nombre"]}\nApellido: {trabajador["apellido"]}\nCargo: {trabajador["cargo"]}\nSueldo Bruto: {trabajador["sueldob"]}\n");
    time.sleep(1);input("Presione ENTER para continuar...")


def planillaSueldos():
    import json;flag4=True;flag5=True;import time
    while flag4:
        print("\n\n\n\n\n\n***** Imprimir planilla de sueldo *****\n")
        try:
            print("1. Imprimir planilla de todos los trabajadores")
            print("2. Imprimir planilla con filtro de empleo")
            opt=int(input("Seleccione opción--> "))
        except:
            print("\n\nDebe ingresar una opción númerica")
        else:
            if opt==1:
                flag4=False
                #todito
                import json;
                try:
                    with open("trabajadores.json", "r") as archivo:
                        trabajadores = json.load(archivo)
                except:
                    print("No existen trabajadores.");
                else:
                    for i in range(len(trabajadores)):
                        trabajador=(trabajadores[i]);
                        print(f"Trabajor: {trabajador["nombre"]} {trabajador["apellido"]}\nCargo: {trabajador["cargo"]}\nSueldo Bruto: {trabajador["sueldob"]}\nDesc. Salud: {trabajador["descuentoSalud"]}\nDesc. AFP: {trabajador["descuentoAFP"]}\nLíquido a Pagar: {trabajador["sueldoL"]}");
                time.sleep(1);input("Presione ENTER para continuar...")

            elif opt==2:
                flag4=False
                while flag5:
                    try:
                        print("\n\n\n\n\n\n***** Seleccionar empleo *****\n")
                        listaCargos=["CEO","Desarrollador","Analista de datos"]
                        for i in range(len(listaCargos)):
                            print(f"{i+1}. {listaCargos[i]}")
                        opt2=int(input("Seleccione opción--> "))
                    except:
                        print("Debe ingresar una opción númerica.")
                    else:
                        if opt2==1:
                            flag5=False
                            try:
                                with open("trabajadores.json", "r") as archivo:
                                    trabajadores = json.load(archivo)
                            except:
                                print("No existen trabajadores.");
                            else:
                                for i in range(len(trabajadores)):
                                    trabajador=(trabajadores[i]);
                                    if(trabajador["cargo"]=="CEO"):
                                        print(f"Trabajor: {trabajador["nombre"]} {trabajador["apellido"]}\nCargo: {trabajador["cargo"]}\nSueldo Bruto: {trabajador["sueldob"]}\nDesc. Salud: {trabajador["descuentoSalud"]}\nDesc. AFP: {trabajador["descuentoAFP"]}\nLíquido a Pagar: {trabajador["sueldoL"]}");
                            time.sleep(1);input("Presione ENTER para continuar...")
                            
                    
                        elif opt2==2:
                            flag5=False
                            try:
                                with open("trabajadores.json", "r") as archivo:
                                    trabajadores = json.load(archivo)
                            except:
                                print("No existen trabajadores.");
                            else:
                                for i in range(len(trabajadores)):
                                    trabajador=(trabajadores[i]);
                                    if(trabajador["cargo"]=="Desarrollador"):
                                        print(f"Trabajor: {trabajador["nombre"]} {trabajador["apellido"]}\nCargo: {trabajador["cargo"]}\nSueldo Bruto: {trabajador["sueldob"]}\nDesc. Salud: {trabajador["descuentoSalud"]}\nDesc. AFP: {trabajador["descuentoAFP"]}\nLíquido a Pagar: {trabajador["sueldoL"]}");
                            time.sleep(1);input("Presione ENTER para continuar...")
                    
                        elif opt2==3:
                            flag5=False
                            try:
                                with open("trabajadores.json", "r") as archivo:
                                    trabajadores = json.load(archivo)
                            except:
                                print("No existen trabajadores.");
                            else:
                                for i in range(len(trabajadores)):
                                    trabajador=(trabajadores[i]);
                                    if(trabajador["cargo"]=="Analista de datos"):
                                        print(f"Trabajor: {trabajador["nombre"]} {trabajador["apellido"]}\nCargo: {trabajador["cargo"]}\nSueldo Bruto: {trabajador["sueldob"]}\nDesc. Salud: {trabajador["descuentoSalud"]}\nDesc. AFP: {trabajador["descuentoAFP"]}\nLíquido a Pagar: {trabajador["sueldoL"]}");
                            time.sleep(1);input("Presione ENTER para continuar...")
                    
                        else:
                            print("SOLO HAY 3 OPCIONES..........................")
            else:
                print("Solo hay 2 opciones.")

