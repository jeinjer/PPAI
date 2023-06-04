from Modelo.cambioEstado import CambioEstado
from datetime import datetime

class Llamada:
    def __init__(self, descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, observacionAuditor,
                 cambioDeEstado, cliente, operador, opcionLlamada, subOpcionSeleccionada):
        self.descripcionOperador = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.cliente = cliente
        self.duracion = duracion
        self.encuestaEnviada = encuestaEnviada
        self.observacionAuditor = observacionAuditor
        self.cambioDeEstado = cambioDeEstado
        self.operador = operador
        self.opcionLlamada = opcionLlamada
        self.subOpcionSeleccionada = subOpcionSeleccionada

    def setDescripcionOperador(self, descripcionOperador):
        self.descripcionOperador = descripcionOperador

    def getDescripcionOperador(self):
        return self.descripcionOperador

    def setDetalleAccionRequerida(self, detalleAccionRequerida):
        self.detalleAccionRequerida = detalleAccionRequerida

    def getDetalleAccionRequerida(self):
        return self.detalleAccionRequerida

    def setDuracion(self, duracion):
        self.duracion = duracion

    def getDuracion(self):
        return self.duracion

    def setObservacionAuditor(self, observacionAuditor):
        self.observacionAuditor = observacionAuditor

    def getObservacionAuditor(self):
        return self.observacionAuditor

    def setCambioDeEstado(self, cambioDeEstado):
        self.cambioDeEstado = cambioDeEstado

    def getCambioDeEstado(self):
        return self.cambioDeEstado

    def setCliente(self, cliente):
        self.cliente = cliente

    def getCliente(self):
        return self.cliente

    def asignarOperador(self, operador):
        self.operador = operador

    def getOperador(self):
        return self.operador

    def setOpcionSeleccionada(self, opcionSeleccionada):
        self.opcionSeleccionada = opcionSeleccionada

    def getOpcionSeleccionada(self):
        return self.opcionSeleccionada

    def setSubopcionSeleccionada(self, subOpcionSeleccionada):
        self.subOpcionSeleccionada = subOpcionSeleccionada

    def getSubOpcionSeleccionada(self):
        return self.subOpcionSeleccionada.getNombre()

    def calcularDuracion(self):
        horaFin = self.cambioDeEstado[-1].getHoraFin()
        horaInicio = self.cambioDeEstado[0].getHoraInicio()

        # Obtener objetos datetime completos para las horas de inicio y fin
        fecha_actual = datetime.today().date()
        inicio_llamada = datetime.combine(fecha_actual, horaInicio)
        fin_llamada = datetime.combine(fecha_actual, horaFin)

        # Calcular la duración de la llamada
        duracion_llamada = fin_llamada - inicio_llamada

        # Obtener los minutos y segundos de la duración
        minutos = duracion_llamada.seconds // 60
        segundos = duracion_llamada.seconds % 60

        # Formatear la duración como "hh:mm"
        duracion_formateada = "{:02d}:{:02d}".format(minutos, segundos)

        # Guardar la duración de la llamada en formato "hh:mm"
        self.duracion = duracion_formateada

    def getNombreClienteLlamada(self):
        return self.cliente.getNombre()

    def setEstadoActual(self, horaInicio, fechaInicio, estado, es_ultimo_estado):
        cambio_estado = CambioEstado(horaInicio, fechaInicio, horaInicio if es_ultimo_estado else None, estado)
        self.cambioDeEstado.append(cambio_estado)

        if len(self.cambioDeEstado) >= 2:
            self.cambioDeEstado[-2].setHoraFin(self.cambioDeEstado[-1].getHoraInicio())

    def finalizarLlamada(self, horaFin, fechaFin, estado, es_ultimo_estado):
        self.setEstadoActual(horaFin, fechaFin, estado, es_ultimo_estado)
        self.calcularDuracion()