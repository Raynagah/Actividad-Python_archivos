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

    








