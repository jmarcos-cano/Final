import sys
import validators
import requests
import time
url ="http://demo7130536.mockable.io/final-contacts-100"
exit = False

peticion = requests.get(url)

contacts = peticion.json()


def agregarcontacto():

    #Iniciar variables-------------
    validacion_nombre = 0
    validacion_telefono = 0
    validacion_email = 0
    #------------------------------

    #Datos del contacto-----------------------------------------------------------------
    input_nombre = input("Ingrese el nombre y apellido del contacto: ")
    input_telefono = input("Ingrese telefono del nuevo contacto: ")
    input_email = input("Ingrese email del nuevo contacto: ")
    input_compañia = input("Ingrese la compañia del nuevo contacto (opcional): ")
    input_nota = input("Ingrese nota del contacto (opcional): ")
    #-----------------------------------------------------------------------------------

    #Validacion del nombre-------------------------------------------------------------
    while(True):
        input_nombre = input_nombre.capitalize()
        if(len(input_nombre.split()) != 2):
            validacion_nombre = 1
        if(validacion_nombre == 1):
            print("\nError del nombre, unicamente tiene que ingresar un nombre y un apellido, ejemplo: Javier Mazariegos\n")
            input_nombre = input("Ingrese el nombre y apellido del contacto: ")
            validacion_nombre = 0
            continue
        else:
            break
    #-----------------------------------------------------------------------------------
    
    #Validacion del telefono------------------------------------------------------------
    while(True):
        if(not input_telefono.isdigit()):
            validacion_telefono = 1
        if(validacion_telefono == 1):
            print("\nError del telefono, el telefono tiene que tener solo numeros, ejemplo: 12345678\n")
            input_telefono = input("Ingrese telefono del nuevo contacto: ")
            validacion_telefono = 0
            continue
        else:
            break
    #-----------------------------------------------------------------------------------

    #Validacion del email---------------------------------------------------------------
    while(True):
        if validators.email(input_email) != True:
            validacion_email = 1
        if(validacion_email == 1):
            print(f"\nError, '{input_email}' no es un correo electronico valido, debes ingresar algo como: ejemplo@example.com\n")
            input_email = input("Ingrese email del nuevo contacto: ")
            validacion_email = 0
            continue
        else:
            break
    #----------------------------------------------------------------------------------

    #Agregar contactos----------------------------------------------------------------------------------------------------------------------
    inicial = input_nombre[0]
    if(inicial in contacts):
        contacts[inicial][input_nombre] = {"telefono":input_telefono, "email": input_email, "company": input_compañia, "extra":input_nota}
    else:
        contacts[inicial] = {input_nombre:{"telefono":input_telefono, "email": input_email, "company": input_compañia, "extra":input_nota}}
    #----------------------------------------------------------------------------------------------------------------------------------------

def buscarcontacto():
    buscar = input("Buscar: ")
    print("Resultados:")
    resultados = 0

    #ciclo para buscar a la persona--------------------------------
    for letra in contacts:
        for persona in contacts[letra]:
            nombre = persona.lower()
            nombre = nombre.split()
            buscar = buscar.lower()
            if(buscar in nombre):
                resultados = 1
                print(f"- {persona}")
    #---------------------------------------------------------------
    if(resultados == 0):
        print("- No hay resultados")


def listaryver():
    #iniciar varaibles------------------------------------------------
    NoContacto = {}
    contador = 0
    #-----------------------------------------------------------------

    #listar contacto--------------------------------------------------
    for letra in contacts:
        print(f"{letra}: ")
        for persona in contacts[letra]:
            contador= contador+1
            print(f"    {contador}. {persona}")
            NoContacto[contador] = persona
    print("\n-------------------------------------")
    vercontacto = int(input("Ver Contacto: "))
    print("\n")
    #------------------------------------------------------------------

    #ver contacto------------------------------------------------------
    for contacto in NoContacto:
        if(vercontacto == contacto):
            nombre = NoContacto[contacto]
            letra = nombre[0]
            telefono = "telefono"
            email = "email"
            company = "company"
            extra = "extra"
            print(f"{NoContacto[vercontacto]}:")
            print(f"    telefono: {contacts[letra][nombre][telefono]}:")
            print(f"    email: {contacts[letra][nombre][email]}:")
            print(f"    company: {contacts[letra][nombre][company]}:")
            print(f"    extra: {contacts[letra][nombre][extra]}:")
    #------------------------------------------------------------------

def borrarcontacto():
    #iniciar variables------------------------------------------------
    NoContacto = {}
    contador = 0
    #-----------------------------------------------------------------

    #listar contactos-------------------------------------------------
    for letra in contacts:
        print(f"{letra}: ")
        for persona in contacts[letra]:
            contador= contador+1
            print(f"    {contador}. {persona}")
            NoContacto[contador] = persona
    print("\n-------------------------")
    contacto = input("Borrar Contacto: ")
    #----------------------------------------------------------------

    #borrar contacto--------------------------------------------------
    if(contacto.isdigit()):
        contacto = int(contacto)
        nombre = NoContacto[contacto]
        letra = nombre[0]
        contacts[letra].pop(nombre)
        print(f"\nContacto '{nombre}' Borrado")
    else:
        letra = contacto[0]
        contacts[letra].pop(contacto)
        print(f"\nContacto '{contacto}' Borrado")
        
    for i in range(3):
        time.sleep(0.5)
    #----------------------------------------------------------------

def llamarcontacto():
    #iniciar variables-----------------------------------------------
    NoContacto = {}
    contador = 0
    #---------------------------------------------------------------

    #listar contactos-----------------------------------------------
    for letra in contacts:
        print(f"{letra}: ")
        for persona in contacts[letra]:
            contador= contador+1
            print(f"    {contador}. {persona}")
            NoContacto[contador] = persona
    print("\n-------------------------------------")
    contacto = input("Llamar Contacto: ")
    #-----------------------------------------------------------------

    #llamar contacto--------------------------------------------------
    if(contacto.isdigit()):
        contacto = int(contacto)
        nombre = NoContacto[contacto]
        letra = nombre[0]
        contacts[letra]
        telefono = "telefono"
        print(f"\nLlamando a '{nombre}' al {contacts[letra][nombre][telefono]}")
    else:
        letra = contacto[0]
        telefono = "telefono"
        print(f"\nLlamando a '{contacto}' al {contacts[letra][contacto][telefono]}")

    for i in range(3):
        time.sleep(0.5)
    #-----------------------------------------------------------------------------------

def enviarmensaje():
    #iniciar variable------------------------------------------------------------------
    NoContacto = {}
    contador = 0
    #-----------------------------------------------------------------------------------

    #listar contacto----------------------------------------------------------------------
    for letra in contacts:
        print(f"{letra}: ")
        for persona in contacts[letra]:
            contador= contador+1
            print(f"    {contador}. {persona}")
            NoContacto[contador] = persona
    print("\n-------------------------------------")
    contacto = input("Contacto: ")
    #-------------------------------------------------------------------------------------

    #Enviar Mensaje-----------------------------------------------------------------------
    if(contacto.isdigit()):
        contacto = int(contacto)
        contacto = NoContacto[contacto]
    print(f"'{contacto}'")
    letra = contacto[0]
    mensaje = input("Mensaje: ")
    telefono = "telefono"
    print(f"\nHola '{contacto}'  {contacts[letra][contacto][telefono]}")
    print(f"      >{mensaje}")
    #---------------------------------------------------------------------------------------


while not exit:
    print("\n----------------------------Menu----------------------------")
    print(" 1. Agregar contacto \n 2. Buscar Contacto\n 3. Listar contacto\n 4. Borrar contacto\n 5. Llamar contactos\n 6. Enviar mensaje a contactos\n 7. Enviar correo a contacto\n 8. Exportar contactos\n 9. Salir")
    print("-----------------------------------------------------------\n")

    input_menu = int(input("Opcion: "))

    if input_menu == 1:
        print("\n----------------Agregar contacto------------------------\n")
        agregarcontacto()
        print("---------------------------------------------------------")
    if input_menu == 2:
        print("\n----------------Buscar contacto------------------------")
        buscarcontacto()
        print("---------------------------------------------------------\n")
    if input_menu == 3:
        print("\n----------------Lista contactos------------------------\n")
        listaryver()
        print("---------------------------------------------------------")
    if input_menu == 4:
        print("\n----------------Borrar contacto------------------------\n")
        borrarcontacto()
        print("---------------------------------------------------------")
    if input_menu == 5:
        print("\n----------------Llamar contacto------------------------\n")
        llamarcontacto()
        print("---------------------------------------------------------")
    if input_menu == 6:
        print("\n----------------Enviar mensaje------------------------\n")
        enviarmensaje()
        print("---------------------------------------------------------")
    if input_menu == 7:
        print("\n----------------Enviar correo------------------------\n")
        pass
        print("---------------------------------------------------------")
    if input_menu == 8:
        print("\n----------------Exportar contactos------------------------")
        pass
        print("---------------------------------------------------------")
    elif input_menu == 9:
        exit = True