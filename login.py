"""
Login
"""

flag = True

lista_user = ["luis1010", "4321"]
lista_user2 = ["marcelo123", "2021"]
lista_user3 = ["juan2020", "6789"]

print("\nLogin")

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

