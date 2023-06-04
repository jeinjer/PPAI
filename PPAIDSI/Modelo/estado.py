class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def estaFinalizada(self):
        return self.getNombre() == "Finalizada"
    
    def estaIniciada(self):
        return self.getNombre() == "Iniciada"
    
    def estaEnCurso(self):
        return self.getNombre() == "En curso"
