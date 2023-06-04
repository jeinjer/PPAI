from Modelo.categoriaLlamada import CategoriaLlamada
from Modelo.opcionLlamada import OpcionLlamada
from Modelo.subOpcionLlamada import SubOpcionLlamada
from Modelo.validacion import Validacion
from Modelo.llamada import Llamada
from Modelo.estado import Estado
from Modelo.cliente import Cliente
from Modelo.cambioEstado import CambioEstado
from Modelo.informacionCliente import InformacionCliente
from datetime import datetime


def crear_llamada_categoria():
    validacion1 = Validacion(audioMensajeValidacion='Audio fecha de nacimiento',
                             nombre='Fecha de nacimiento')

    validacion2 = Validacion(audioMensajeValidacion='Audio cantidad hijos',
                             nombre='Cantidad de hijos')

    info1 = InformacionCliente(datoAValidar=None,
                               datoCorrecto='12-5-1999',
                               validacion=validacion1)

    info2 = InformacionCliente(datoAValidar=None,
                               datoCorrecto='1',
                               validacion=validacion2)

    cliente1 = Cliente(dni='12345678',
                       nombre='Juan Perez',
                       nroCelular='35415533221',
                       informacionCliente=[info1, info2])

    subopcion_llamada1 = SubOpcionLlamada(nombre='Hablar con operador',
                                          nroOrden='1',
                                          validacionesRequeridas=[validacion1, validacion2])

    opcion1 = OpcionLlamada(audioMensajeSubOpciones=None,
                            mensajeSubOpciones='',
                            nombre='Informar robo',
                            nroOrden='2',
                            subOpcionLlamada=None,
                            validacionesRequeridas=None)
    
    opcion2 = OpcionLlamada(audioMensajeSubOpciones=None,
                            mensajeSubOpciones='',
                            nombre='Desbloquear tarjeta',
                            nroOrden='3',
                            subOpcionLlamada=None,
                            validacionesRequeridas=None)

    opcion3 = OpcionLlamada(audioMensajeSubOpciones=None,
                            mensajeSubOpciones='',
                            nombre='Asistencia Técnica',
                            nroOrden='1',
                            subOpcionLlamada=subopcion_llamada1,
                            validacionesRequeridas=[validacion1, validacion2])

    cambio_estado1 = CambioEstado(hora_inicio=datetime.now().time(),
                                  fecha_inicio=datetime.now().date(),
                                  hora_fin=None,
                                  estado='Iniciada')

    categoria_llamada1 = CategoriaLlamada(audioMensajeOpciones = None,
                                          mensajeOpciones='',
                                          nombre='Robo y seguridad',
                                          nroOrden='5',
                                          opcion=opcion1)

    categoria_llamada3 = CategoriaLlamada(audioMensajeOpciones=None,
                                          mensajeOpciones='',
                                          nombre='Categoria Ayuda',
                                          nroOrden='5',
                                          opcion=opcion3)
    
    categoria_llamada2 = CategoriaLlamada(audioMensajeOpciones=None,
                                          mensajeOpciones='',
                                          nombre='Estado de la tarjeta',
                                          nroOrden='2',
                                          opcion=opcion2)

    llamada = Llamada(descripcionOperador='Sin observacion',
                       detalleAccionRequerida='Sin detalle de accion',
                       encuestaEnviada='Encuesta nº23',
                       observacionAuditor='Es correcto',
                       cambioDeEstado=[cambio_estado1],
                       cliente=cliente1,
                       opcionLlamada=opcion3,
                       subOpcionSeleccionada=subopcion_llamada1,
                       operador=None,
                       duracion='00:38')

    return llamada


def crear_estados():
    listaEstados = []

    estado1 = Estado('Cancelada')
    estado2 = Estado('Finalizada')
    estado3 = Estado('Iniciada')
    estado4 = Estado('En curso')

    listaEstados.extend([estado1, estado2, estado3, estado4])

    return listaEstados
