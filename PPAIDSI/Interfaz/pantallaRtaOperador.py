import tkinter as tk
from tkinter import messagebox

class PantallaRtaOperador:
    def __init__(self, ventana, gestor):
        self.lblDetalleAccionRegistrada = None
        self.rdbtn1 = None
        self.rdbtn2 = None
        self.rdbtn3 = None
        self.rdbtn4 = None
        self.rdbtn5 = None
        self.rdbtn6 = None
        self.botonSolicitarValidacion = None
        self.lblValidacion1 = None
        self.lblValidacion2 = None
        self.gestor = gestor
        self.lblTxtOperador = tk.Label(ventana, text='Ingrese consulta del cliente', font='Arial 14', bg='lightyellow', relief='solid')
        self.txtAreaRespuestaOperador = tk.Text(ventana)
        self.btnEnviarInfoOperador = tk.Button(ventana, text='Enviar informacion', font='bold', bg='#d2b48c', relief='solid')
        self.opcionSeleccionada1 = None
        self.opcionSeleccionada2 = None
        self.botonEnviarValidacion = None
        self.seleccion = None
        self.ventana = ventana
        self.btnCancelar = tk.Button(ventana, text='Cancelar', font='bold', bg='indian red', command=self.ventana.destroy)
        self.btnConfirmar = tk.Button(ventana, text='Confirmar', font='bold', bg='lightyellow')
        self.lblCategoria = None
        self.lblOpcion = None
        self.lblSubOpcion = None
        self.lblCliente = None
        self.respuesta = None

    def mostrarDatosObtenidos(self, cliente, opcion, subopcion, categoria, validaciones):

        texto_llamada = 'Datos de la llamada'
        texto_llamada = tk.Label(
                                 self.ventana,
                                 text=texto_llamada,
                                 font='Nunito 16 bold',
                                 borderwidth=10,
                                 bg='peachpuff',
                                 relief='ridge')
        texto_llamada.grid(row = 1, column = 0, sticky="w", padx=5, pady=5)

        texto_cat = 'Categoria: ' + categoria.split()[1]
        self.lblCategoria = tk.Label(self.ventana,
                                     text=texto_cat,
                                     font='Nunito 13 bold',
                                     borderwidth=12,
                                     bg='peachpuff',
                                     )
        self.lblCategoria.grid(row= 2, column=0, sticky="w", padx=10, pady=10)

        texto_opc = 'Opcion: ' + opcion
        self.lblOpcion = tk.Label(
                                  self.ventana,
                                  text=texto_opc,
                                  font='Nunito 13 bold',
                                  borderwidth=12,
                                  bg='peachpuff')
        self.lblOpcion.grid(row= 3, column=0, sticky="w", padx=10, pady=10)

        texto_subopc = 'Subopcion: ' + subopcion
        self.lblSubOpcion = tk.Label(
                                     self.ventana,
                                     text=texto_subopc,
                                     font='Nunito 13 bold',
                                     borderwidth=12,
                                     bg='peachpuff')
        self.lblSubOpcion.grid(row= 4, column=0, sticky="w", padx=10, pady=10)

        texto_cliente = 'Cliente: ' + cliente
        self.lblCliente = tk.Label(
                                   self.ventana,
                                   text=texto_cliente,
                                   font='Nunito 13 bold',
                                   borderwidth=12,
                                   bg='peachpuff')
        self.lblCliente.grid(row=5, column=0, sticky="w", padx=10, pady=10)

        self.botonSolicitarValidacion = tk.Button(
                                                  self.ventana,
                                                  text='Solicitar validacion a cliente',
                                                  font='Calibri 13 bold',
                                                  borderwidth=16,
                                                  bg='#ccffe6',
                                                  command=lambda: self.solicitarDatosAValidar(validaciones),
                                                  width=25,
                                                  height=2)
        self.botonSolicitarValidacion.place(x=450, y=180)

    def solicitarDatosAValidar(self, validaciones):
        self.botonSolicitarValidacion.destroy()

        self.opcionSeleccionada1 = tk.StringVar()
        self.opcionSeleccionada1.set(None)

        self.opcionSeleccionada2 = tk.StringVar()
        self.opcionSeleccionada2.set(None)

        self.lblValidacion1 = tk.Label(self.ventana,
                                       text=validaciones[0] + " (dd-mm-aaaa)",
                                       bg='lightyellow',
                                       font='bold')
        self.lblValidacion1.place(x=500, y=30)

        self.rdbtn1 = tk.Radiobutton(self.ventana,
                                     text='15-2-1988',
                                     font='bold',
                                     variable=self.opcionSeleccionada1,
                                     value='15-2-1988',
                                     bg='peachpuff')
        self.rdbtn1.place(x=500, y=60)
        self.rdbtn2 = tk.Radiobutton(self.ventana, text='5-12-1998',
                                     variable=self.opcionSeleccionada1,
                                     font='bold',
                                     value='5-12-1988',
                                     bg='peachpuff')
        self.rdbtn2.place(x=500, y=80)
        self.rdbtn3 = tk.Radiobutton(self.ventana,
                                     text='12-5-1999',
                                     font='bold',
                                     bg='peachpuff',
                                     variable=self.opcionSeleccionada1,
                                     value='12-5-1999')
        self.rdbtn3.place(x=500, y=100)

        self.lblValidacion2 = tk.Label(self.ventana,
                                       text=validaciones[1],
                                       bg='lightyellow',
                                       font='bold')
        self.lblValidacion2.place(x=500, y=135)

        self.rdbtn4 = tk.Radiobutton(self.ventana,
                                     text='0',
                                     font='bold',
                                     bg='peachpuff',
                                     variable=self.opcionSeleccionada2,
                                     value=0)
        self.rdbtn4.place(x=500, y=160)

        self.rdbtn5 = tk.Radiobutton(self.ventana,
                                     text='1',
                                     font='bold',
                                     bg='peachpuff',
                                     variable=self.opcionSeleccionada2,
                                     value=1)
        self.rdbtn5.place(x=500, y=180)

        self.rdbtn6 = tk.Radiobutton(self.ventana,
                                     text='2',
                                     font='bold',
                                     bg='peachpuff',
                                     variable=self.opcionSeleccionada2,
                                     value=2)
        self.rdbtn6.place(x=500, y=200)

        self.botonEnviarValidacion = tk.Button(self.ventana,
                                               text='Enviar validacion',
                                               font='bold',
                                               bg='lightgreen',
                                               command=lambda:
                                               self.tomarRespuestaValidacion(self.opcionSeleccionada1.get(),
                                                                             self.opcionSeleccionada2.get(),
                                                                             validaciones))
        self.botonEnviarValidacion.place(x=500, y=240)
        self.btnCancelar.place(x=650, y=240)  # Alternativa de CU

    def tomarRespuestaValidacion(self, res1, res2, v):
        if res1 == 'None' or res2 == 'None':
            messagebox.showwarning('Advertencia', 'Debes completar el/los campos')
        else:
            messagebox.showinfo('Éxito', 'Se ha enviado la información')
            self.gestor.tomarRespuestaValidacion(res1, res2, v)

            self.lblValidacion1.destroy()
            self.lblValidacion2.destroy()
            self.rdbtn1.destroy()
            self.rdbtn2.destroy()
            self.rdbtn3.destroy()
            self.rdbtn4.destroy()
            self.rdbtn5.destroy()
            self.rdbtn6.destroy()
            self.botonEnviarValidacion.destroy()
            self.btnCancelar.destroy()

    def solicitarConfirmacion(self):
        self.btnConfirmar.config(width=15, height=2, command=self.gestor.confirmar)
        self.btnConfirmar.place(x=430, y=100)

    def tomarConfirmacion(self):
        self.gestor.confirmar()

    def solicitarRespuestaOperador(self):
        self.txtAreaRespuestaOperador.config(width=30, height=2)
        self.txtAreaRespuestaOperador.bind("<Key>", lambda event:
                                                                self.txtAreaRespuestaOperador.delete("end-2c", "end-1c")
                                                                if len(self.txtAreaRespuestaOperador.get("1.0", "end-1c")) >= 35
                                                                else None)
        self.txtAreaRespuestaOperador.place(x=400, y=60)
        self.lblTxtOperador.place(x=400, y=30)
        self.btnEnviarInfoOperador.place(x=400, y=150)
        self.btnEnviarInfoOperador.config(command=lambda: self.tomarRespuestaOperador(
            self.txtAreaRespuestaOperador.get('1.0', 'end-1c')))

    def tomarRespuestaOperador(self, respuesta):
        if not respuesta.strip():
            messagebox.showwarning('Advertencia', 'No se ha ingresado ninguna respuesta')
            self.solicitarRespuestaOperador()
        else:
            messagebox.showinfo('Exito', 'Se ha enviado tu respuesta')
            self.txtAreaRespuestaOperador.destroy()
            self.lblTxtOperador.destroy()
            self.btnEnviarInfoOperador.destroy()
            self.gestor.tomarRespuestaOperador(respuesta)

    def informarAccionRegistrada(self, detalle):
        self.btnConfirmar.destroy()
        self.lblDetalleAccionRegistrada = tk.Label(self.ventana,
                                                   text=detalle,
                                                   font='Roboto 14',
                                                   wraplength=0,
                                                   bg='lightyellow')
        self.lblDetalleAccionRegistrada.place(x=300, y=100)
