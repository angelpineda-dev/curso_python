# Obtener elementos

diccionario = {'a':1, 'b':2, 'c':3, 'd':4, }

# Obtener valor
valor = diccionario['d']

# Saber si el valor existe
is_valor = 'a' in diccionario

# Valor por defecto
valor = diccionario.get('t', 'key not found')

# metodo setdefault() - permite obtener el valor de una llave, si no existe, la crea con un valor.

valor = diccionario.setdefault('e', 5)

print(valor)
print(is_valor)
print(diccionario)