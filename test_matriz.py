import json


nombre = input("Agregue el nombre: ")
apellido = input("Agregue el apellido: ")
cargo = input("Agregue el cargo del trabajador: ")
sueldob = input("Agregue el sueldo bruto del trabajador: ")



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


