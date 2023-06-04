import random as r

# Probabilidad aleatoria del 20% de que el CU 28 falle (alternativa de CU)
def crearDetalleAccionRequerida(respuestaOperador):
    if r.randint(1, 5) != 5:
        return f'El operador ha dicho: {respuestaOperador}'
    return -1
