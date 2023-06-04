class OpcionLlamada:
    def __init__(self, audioMensajeSubOpciones, mensajeSubOpciones, nombre, nroOrden, subOpcionLlamada, validacionesRequeridas):
        self.audioMensajeSubOpciones = audioMensajeSubOpciones
        self.mensajeSubOpciones = mensajeSubOpciones
        self.nombre = nombre
        self.nroOrden = nroOrden
        self.subOpcionLlamada = subOpcionLlamada
        self.validacionesRequeridas = validacionesRequeridas

    def setAudioMensajeSubOpciones(self, audioMensajeSubOpciones):
        self.audioMensajeSubOpciones = audioMensajeSubOpciones

    def getAudioMensajeSubOpciones(self):
        return self.audioMensajeSubOpciones
    
    def setMensajeSubOpciones(self, mensajeSubOpciones):
        self.mensajeSubOpciones = mensajeSubOpciones

    def getMensajeSubOpciones(self):
        return self.mensajeSubOpciones
    
    def setNomOpcLlamada(self, nombre):
        self.nombre = nombre

    def getNomOpcLlamada(self):
        return self.nombre
    
    def setNroOrden(self, nroOrden):
        self.nroOrden = nroOrden

    def getNroOrden(self):
        return self.nroOrden
    
    def setSubOpcionLlamada(self, subOpcionLlamada):
        self.subOpcionLlamada = subOpcionLlamada

    def getSubOpcionLlamada(self):
        return self.subOpcionLlamada
    
    def setValidacionesRequeridas(self, validacionesRequeridas):
        self.validacionesRequeridas = validacionesRequeridas

    def getValidacionesRequeridas(self):
        return self.validacionesRequeridas

    def esOpcion(self):
        return isinstance(self, OpcionLlamada)

