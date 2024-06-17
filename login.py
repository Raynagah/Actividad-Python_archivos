"""
Login
"""

flag = True

lista_user = ["luis1010", "4321"]
lista_user2 = ["marcelo123", "2021"]
lista_user3 = ["juan2020", "6789"]

while flag:

    print("\nLogin")
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    if user == lista_user[0] and password == lista_user[1]:
        print(f"El {user} ")
    elif user == lista_user2[0] and password == lista_user2[1]:
        print(f"El {user} ")
    elif user == lista_user3[0] and password == lista_user3[1]:
        print(f"El {user} ")
    else:
        print("Vuelva a intentarlo...")
