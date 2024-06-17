import json

nombre=input("Agregue el nombre: ")
apellido=input("Agregue el apellido: ")
cargo=input("Agregue el cargo del trabajador: ")
sueldob=input("Agregue el sueldo bruto del trabajador: ")
#VALIDAR ENTRADA DE DATOS


#Agregar a la lista
trabajador=[{"nombre": nombre, "apellido":apellido,"cargo":cargo,"sueldob":sueldob}]

archivojson="trabajadores.json"

with open(archivojson, "w") as archivo:
    json.dump(trabajador,archivo,indent=4)


