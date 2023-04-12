class Email:
    def __init__(self, idCuenta, dominio, tipoDominio, contraseña):
        self.idCuenta = idCuenta
        self.dominio = dominio
        self.tipoDominio = tipoDominio
        self.contraseña = contraseña

    def retornaEmail(self):
        return f"{self.idCuenta}@{self.dominio}.{self.tipoDominio}"

    def getDominio(self):
        return self.dominio

    def crearCuenta(self, direccionCorreo):
        partes = direccionCorreo.split("@")
        if len(partes) == 2:
            idCuenta, dominio_tipoDominio = partes
            dominio, tipoDominio = dominio_tipoDominio.split(".")
            contraseña = input("Ingrese la contraseña: ")
            if contraseña == self.contraseña:
                self.idCuenta = idCuenta
                self.dominio = dominio
                self.tipoDominio = tipoDominio
                print("Cuenta creada exitosamente.")
            else:
                print("Contraseña incorrecta.")
        else:
            print("Dirección de correo inválida.")