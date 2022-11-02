# Diccionarios

# Creando diccionario
elementos = {}

# Agregando elementos
elementos['nombre'] = 'Jose Luis'
elementos[(1,2,3)] = 'La llave es una tupla'

# Modificar llaves - Si la llave no existe, python la crea de lo contrario, actualiza su valor.
elementos['nombre'] = 'Cody'


print(elementos)
# Longitud de un diccionario
print('longitud: ', len(elementos))