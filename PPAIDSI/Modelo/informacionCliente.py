class InformacionCliente:
    def __init__(self, datoAValidar, datoCorrecto, validacion):
        self.datoAValidar = datoAValidar
        self.opcionCorrecta = datoCorrecto
        self.validacion = validacion

    def setDatoAValidar(self, datoAValidar):
        self.datoAValidar = datoAValidar

    def getDatoAValidar(self):
        return self.datoAValidar
    
    def setOpcionCorrecta(self, opcionCorrecta):
        self.opcionCorrecta = opcionCorrecta

    def getOpcionCorrecta(self):
        return self.opcionCorrecta

    def esInformacionCorrecta(self, respuesta):
        return respuesta == self.opcionCorrecta

    def esValidacion(self, validaciones):
        return self.validacion.nombre in validaciones
