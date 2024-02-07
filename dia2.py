cantidad_usuarios = int(input("¿Cuántos usuarios desea registrar? "))

for i in range(cantidad_usuarios):
    print("\nRegistro del usuario", i + 1)

    nombre = input("Ingrese su nombre: ")
    while not (5 <= len(nombre) <= 50):
        print("El nombre debe tener entre 5 y 50 caracteres.")
        nombre = input("Ingrese su nombre nuevamente: ")

    apellidos = input("Ingrese sus apellidos: ")
    while not (5 <= len(apellidos) <= 50):
        print("Los apellidos deben tener entre 5 y 50 caracteres.")
        apellidos = input("Ingrese sus apellidos nuevamente: ")

    telefono = input("Ingrese su número de teléfono (10 dígitos): ")
    while not (len(telefono) == 10 and telefono.isdigit()):
        print("El número de teléfono debe tener 10 dígitos numéricos.")
        telefono = input("Ingrese su número de teléfono nuevamente: ")

    correo = input("Ingrese su correo electrónico: ")
    while not (5 <= len(correo) <= 50 and '@' in correo and '.' in correo):
        print("El correo electrónico debe tener entre 5 y 50 caracteres y tener un formato válido.")
        correo = input("Ingrese su correo electrónico nuevamente: ")

    print("Usuario registrado con éxito:")
    print("Nombre:", nombre)
    print("Apellidos:", apellidos)
    print("Teléfono:", telefono)
    print("Correo electrónico:", correo)