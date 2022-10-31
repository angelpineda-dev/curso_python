# Concatenar

nombre = 'Eduardo Ismael'
apellido = 'Garcia'

# Concatenacion con el simbolo de suma ( + )
## nombre_completo = nombre + ' ' + apellido + '.'

# Segunda forma de concatenar es con %s, donde se crea un String base y 
# las variables agregadas dentro del parentesis sustituiran a los elementos de %s.
nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Martinez')
print(nombre_completo)