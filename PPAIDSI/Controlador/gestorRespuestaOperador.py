from datetime import datetime
import CU.cu28 as cu28
from tkinter import messagebox
from Modelo.categoriaLlamada import CategoriaLlamada


class Gestor:
    def __init__(self, llamada, pantallaRtaOperador, listaEstados):
        self.respuestaOperador = None
        self.listaCategorias = None
        self.fechaActual = None
        self.horaActual = None
        self.llamada = llamada
        self.pantallaRtaOperador = pantallaRtaOperador
        self.listaEstados = listaEstados
        self.respuestaValidacion = None
        self.cliente = llamada.cliente

    def opcComunicarOperador(self):
        self.identificarLlamada()

    def identificarLlamada(self):
        self.buscarEstadoEnCurso()

    def buscarEstadoEnCurso(self):
        for estado in self.listaEstados:
            if estado.estaEnCurso():
                self.llamada.asignarOperador('Juan Perez')
                self.llamada.setEstadoActual(horaInicio=datetime.now().time(),
                                             fechaInicio=datetime.now().date(),
                                             estado=estado,
                                             es_ultimo_estado=False)
                break

        self.buscarDatosLlamada()

    def buscarDatosLlamada(self):
        cliente = self.llamada.getNombreClienteLlamada()
        opcion_llamada = self.llamada.opcionLlamada.getNomOpcLlamada()
        subopcion_llamada = self.llamada.opcionLlamada.subOpcionLlamada.getNomSubOpcLlamada()
        validaciones = self.llamada.opcionLlamada.subOpcionLlamada.getValidaciones()
        categoria_seleccionada = ''
        
        if self.llamada.opcionLlamada.esOpcion():

            self.listaCategorias = CategoriaLlamada.getCategoria()

            for categoria in self.listaCategorias:
                if categoria.opcion.getNomOpcLlamada() == opcion_llamada:
                    categoria_seleccionada = categoria.getNombre()

        self.pantallaRtaOperador.mostrarDatosObtenidos(cliente, opcion_llamada,
                                                       subopcion_llamada, categoria_seleccionada, validaciones)

    def tomarRespuestaValidacion(self, res1, res2, validaciones):
        self.validarInfoCorrecta(res1, res2, validaciones)

    def validarInfoCorrecta(self, res1, res2, validaciones):
        respuestas = self.cliente.esCliente(res1, res2, validaciones)

        # Alternativa de CU
        if False in respuestas:
            messagebox.showerror('Error', 'Hay un error de respuestas/validacion. Se cancela el Caso de Uso')
            exit()

        else:
            self.pantallaRtaOperador.solicitarRespuestaOperador()

    def tomarRespuestaOperador(self, respuesta):
        self.respuestaOperador = respuesta
        self.pantallaRtaOperador.solicitarConfirmacion()

    def confirmar(self):
        detalle = cu28.crearDetalleAccionRequerida(self.respuestaOperador)

        if detalle != -1:
            self.llamada.detalleAccionRequerida = detalle
            self.pantallaRtaOperador.informarAccionRegistrada(self.llamada.detalleAccionRequerida)
            self.finalizarLlamada()

        else:
            messagebox.showerror('Error', 'El CU 28 no se ha podido ejecutar con exito. Se cancela el CU')
            exit()

    def finalizarLlamada(self):
        self.getHoraFechaActual()

    def getHoraFechaActual(self):
        self.fechaActual = datetime.now().date()
        self.horaActual = datetime.now().time()
        self.buscarEstadoFinalizado()

    def buscarEstadoFinalizado(self):
        for estado in self.listaEstados:
            if estado.estaFinalizada():
                self.llamada.finalizarLlamada(self.horaActual, self.fechaActual, estado.getNombre(), True)
                break

        self.finCU()

    def finCU(self):
        messagebox.showinfo('Llamada finalizada', f'Duracion de la llamada: {self.llamada.duracion}')
        exit()
