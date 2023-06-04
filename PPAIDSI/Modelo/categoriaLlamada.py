class CategoriaLlamada:
    categorias = []
    def __init__(self, audioMensajeOpciones, mensajeOpciones, nombre, nroOrden, opcion):
        self.audioMensajeOpciones = audioMensajeOpciones
        self.mensajeOpciones = mensajeOpciones
        self.nombre = nombre
        self.nroOrden = nroOrden
        self.opcion = opcion
        self.categorias.append(self)

    def setAudioMensajeOpciones(self, audioMensajeOpciones):
        self.audioMensajeOpciones = audioMensajeOpciones

    def getAudioMensajeOpciones(self):
        return self.audioMensajeOpciones
    
    def setMensajeOpciones(self, mensajeOpciones):
        self.mensajeOpciones = mensajeOpciones

    def getMensajeOpciones(self):
        return self.mensajeOpciones
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setNroOrden(self, nroOrden):
        self.nroOrden = nroOrden

    def getNroOrden(self):
        return self.nroOrden
    
    def setOpcion(self, opcion):
        self.opcion = opcion

    def getOpcion(self):
        return self.opcion
    
    @classmethod
    def getCategoria(cls):
        return cls.categorias 
