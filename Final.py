import requests

url ="http://demo7130536.mockable.io/final-contacts-100"
exit = False

peticion = requests.get(url)

contacts = peticion.json()

while not exit:
    print("\n----------------------------Menu----------------------------")
    print(" 1. Agregar contacto \n 2. Buscar Contacto\n 3. Listar contacto\n 4. Borrar contacto\n 5. Llamar contactos\n 6. Enviar mensaje a contactos\n 7. Enviar correo a contacto\n 8. Exportar contactos\n 9. Salir")
    print("-----------------------------------------------------------\n")

    input_menu = int(input("Opcion: "))

    if input_menu == 1:
        print("\n----------------Agregar contacto------------------------\n")
        pass
        print("---------------------------------------------------------")
    if input_menu == 2:
        print("\n----------------Buscar contacto------------------------")
        pass
        print("---------------------------------------------------------\n")
    if input_menu == 3:
        print("\n----------------Lista contactos------------------------\n")
        pass
        print("---------------------------------------------------------")
    if input_menu == 4:
        print("\n----------------Borrar contacto------------------------\n")
        pass
        print("---------------------------------------------------------")
    if input_menu == 5:
        print("\n----------------Llamar contacto------------------------\n")
        pass
        print("---------------------------------------------------------")
    if input_menu == 6:
        print("\n----------------Enviar mensaje------------------------\n")
        pass
        print("---------------------------------------------------------")
    if input_menu == 7:
        print("\n----------------Enviar correo------------------------\n")
        pass
        print("---------------------------------------------------------")
    if input_menu == 8:
        print("\n----------------Enviar correo------------------------")
        pass
        print("---------------------------------------------------------")
    elif input_menu == 9:
        exit = True