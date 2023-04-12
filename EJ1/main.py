from correo import Email
from imprimir_mensaje import imprimir_mensaje


# Ingreso de datos por teclado
idCuenta = input("Ingrese el id de cuenta: ")
dominio = input("Ingrese el dominio: ")
tipoDominio = input("Ingrese el tipo de dominio: ")
contraseña = input("Ingrese la contraseña: ")

# Creación de instancia de la clase Email
email = Email(idCuenta, dominio, tipoDominio, contraseña)

# Imprimir mensaje
nombre = input("Ingrese su nombre: ")
imprimir_mensaje(nombre, email.retornaEmail())

# Modificar contraseña
contraseña_actual = input("Ingrese la contraseña actual: ")
if contraseña_actual == email.contraseña:
    nueva_contraseña = input("Ingrese la nueva contraseña: ")
    email.contraseña = nueva_contraseña
    print("Contraseña modificada exitosamente.")
else:
    print("Contraseña incorrecta.")

# Crear objeto de clase Email a partir de una dirección de correo
direccionCorreo = input("Ingrese una dirección de correo: ")
email.crearCuenta(direccionCorreo)




# Leer archivo separado por comas
cuentas_creadas = []  # Inicializar lista de cuentas creadas
with open("direcciones.csv", "r") as archivo:
    direcciones = archivo.read().split(",")
    for direccion in direcciones:
        partes = direccion.split("@")
        if len(partes) == 2:
            idCuenta = partes[0]
            dominio_tipoDominio = partes[1].split(".")
            if len(dominio_tipoDominio) == 2:
                dominio = dominio_tipoDominio[0]
                tipoDominio = dominio_tipoDominio[1]
                nueva_cuenta = Email(idCuenta, dominio, tipoDominio, "password")
                cuentas_creadas.append(nueva_cuenta)  # Agregar cuenta creada a la lista
                print(f"Cuenta creada exitosamente: {nueva_cuenta.retornaEmail()}")
            else:
                print(f"Dirección de correo inválida: {direccion}")
        else:
            print(f"Dirección de correo inválida: {direccion}")


# Contar objetos de la clase Email con dominio igual al ingresado
dominio_buscar = input("Ingrese un dominio: ")
contador = 0
for cuenta in cuentas_creadas:
    if cuenta.dominio == dominio_buscar:
        contador += 1

# Mostrar el resultado
print(f"El dominio '{dominio_buscar}' se encuentra en {contador} cuentas creadas.")



#OTRA FORMA DE HACERLO
# # Leer archivo separado por comas
# with open("direcciones.csv", "r") as archivo:
#     direcciones = archivo.read().split(",")
#     for direccion in direcciones:
#         email_cuenta = direccion.split("@")[0]
#         email_dominio = direccion.split("@")[1].split(".")[0]
#         email_tipoDominio = direccion.split("@")[1].split(".")[1]
#         nueva_cuenta = Email(email_cuenta, email_dominio, email_tipoDominio, "password")
#         print(f"Cuenta creada exitosamente: {nueva_cuenta.retornaEmail()}")
