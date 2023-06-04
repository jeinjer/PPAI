class CambioEstado:
    def __init__(self, hora_inicio, fecha_inicio, hora_fin, estado):
        self.fecha_inicio = fecha_inicio
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado

    def setFechaInicio(self, fecha):
        self.fecha_inicio = fecha

    def getFechaInicio(self):
        return self.fecha_inicio
    
    def setHoraInicio(self, hora):
        self.hora_inicio = hora

    def getHoraInicio(self):
        return self.hora_inicio
    
    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def setHoraFin(self, hora):
        self.hora_fin = hora

    def getHoraFin(self):
        return self.hora_fin
