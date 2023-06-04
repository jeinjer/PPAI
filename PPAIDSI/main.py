from Controlador.gestorRespuestaOperador import Gestor
from Interfaz.pantallaRtaOperador import PantallaRtaOperador
import CU.cu1 as c
import tkinter as tk

'''
Hay que crear la llamada, categoria, opcion y sub-opcion (si corresponde)
que se crea desde el CU 1 Registrar Llamada, donde la llamada se crea al momento de iniciarse
y se asocia al cliente, y donde la categoria y opciones son seleccionadas por dicho cliente.
'''

llamada = c.crear_llamada_categoria()
listaEstados = c.crear_estados()

ventana = tk.Tk()
ventana.title('Registrar respuesta de operador')
ventana.resizable(0, 0)
ventana.geometry('860x340')
ventana.config(bg='peachpuff')

pantalla = PantallaRtaOperador(ventana=ventana, gestor=None)

gestor = Gestor(llamada=llamada,
                pantallaRtaOperador=pantalla,
                listaEstados=listaEstados)

pantalla.gestor = gestor
gestor.opcComunicarOperador()
ventana.mainloop()
