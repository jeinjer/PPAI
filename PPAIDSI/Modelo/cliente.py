class Cliente:
    def __init__(self, dni, nombre, nroCelular, informacionCliente):
        self.dni = dni
        self.nombreCompleto = nombre
        self.informacionCliente = informacionCliente
        self.nroCelular = nroCelular

    def setDni(self, dni):
        self.dni = dni

    def getDni(self):
        return self.dni
    
    def setNombre(self, nombre):
        self.nombreCompleto = nombre

    def getNombre(self):
        return self.nombreCompleto

    def setInfo(self, info):
        self.informacionCliente = info

    def getInfo(self):
        return self.informacionCliente

    def esCliente(self, res1, res2, validaciones):
        datos = [res1, res2]
        respuestas = []
        for i in range(len(self.informacionCliente)):
            if self.informacionCliente[i].esInformacionCorrecta(datos[i]):
                respuestas.append(True)
            else:
                respuestas.append(False)

            if self.informacionCliente[i].esValidacion(validaciones):
                respuestas.append(True)
            else:
                respuestas.append(False)

        return respuestas
