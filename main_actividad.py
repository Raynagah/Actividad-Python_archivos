import csv;
import time as tiempo;

#definimos las variables 
cargo="";
sueldo_bruto=0;
desc_salud=sueldo_bruto*0.07;
dec_afp=sueldo_bruto*0.12;
liquido_a_pagar=0;

lista_trabajadores=[];
lista_cargos=["CEO","Jefe de área","Obrero","Contador"];

bandera_menu=True;

"""
Login
"""

flag = True

lista_user = ["luis1010", "4321"]
lista_user2 = ["marcelo123", "2021"]
lista_user3 = ["juan2020", "6789"]

print("\n~~~Login~~~")

while flag:

    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    if user == lista_user[0] and password == lista_user[1]:
        print(f"\nEl usuario {user} ha ingresado correctamente.\n")
        flag = False

    elif user == lista_user2[0] and password == lista_user2[1]:
        print(f"\nEl usuario {user} ha ingresado correctamente.\n")
        flag = False

    elif user == lista_user3[0] and password == lista_user3[1]:
        print(f"\nEl usuario {user} ha ingresado correctamente.\n")
        flag = False

    else:
         print("Vuelva a intentarlo...\n")

while bandera_menu:
    print("\n*****Elige una de las siguientes opciones*****\n");
    print("1.Registrar Trabajador");
    print("2.Listar todos los trabajadores");
    print("3.Imprimir planilla de sueldos");
    print("4.Salir del programa");
    try:
        opcion=int(input("Ingrese la opción deseada: "));
    except:
        print("La opción ingresada no es válida, intentalo nuevamente");
    else: 
        if opcion==1:
            print("Eligió Registrar Trabajador");
        elif opcion==2:
            print("Eligió Listar todos los trbajadores");
        elif opcion==3:
            print("Eligió Imprimir planilla de sueldos");
        elif opcion==4:
            print("Eligió Salir, gracias por utilizar nuestro programa");
            bandera_menu=False;
        else:
            print("La opción ingresada no es válida, intentelo nuevamente");

    








