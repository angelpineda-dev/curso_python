# Justificar texto

mensaje = 'Hola mundo!'

# No modifican al string original, solo generan uno nuevo, los metodos recibe como parametro los espacios que deseamos agregar.

# metodo ljust -> justifica a la izquierda
mensaje_left = mensaje.ljust(20)
print(mensaje_left,'.')
# metodo rjust -> justifica a la derecha
mensaje_right = mensaje.rjust(20)
print(mensaje_right,'.')
# metodo center -> justifica al centro
mensaje_center = mensaje.center(20)
print(mensaje_center,'.')