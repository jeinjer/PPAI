class SubOpcionLlamada:
    def __init__(self, nombre, nroOrden, validacionesRequeridas):
        self.nombre = nombre
        self.nroOrden = nroOrden
        self.validacionesRequeridas = validacionesRequeridas

    def setNomSubOpcLlamada(self, nombre):
        self.nombre = nombre

    def getNomSubOpcLlamada(self):
        return self.nombre
    
    def setNroOrden(self, nroOrden):
        self.nroOrden = nroOrden

    def getNroOrden(self):
        return self.nroOrden
    
    def setNombValidacion(self, validacionesRequeridas):
        self.validacionesRequeridas = validacionesRequeridas

    def getValidaciones(self):
        lista_validaciones = []

        for validacion in self.validacionesRequeridas:
            lista_validaciones.append(validacion.getNombreValidacion())

        return lista_validaciones

