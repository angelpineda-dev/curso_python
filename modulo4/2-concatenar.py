# Concatenar

nombre = 'Eduardo Ismael'
apellido = 'Garcia'

# Concatenacion con el simbolo de suma ( + )
## nombre_completo = nombre + ' ' + apellido + '.'

# Segunda forma de concatenar es con %s, donde se crea un String base y 
# las variables agregadas dentro del parentesis sustituiran a los elementos de %s.
## nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Martinez')

# format - mediante un String base generaremos un nuevo string y con la ayuda de placeholders {}

## nombre_completo = "Mr. {} {} {}".format(nombre, apellido, 'Perez')

# Es posible nombrar los placesholders, agregando un nombre dentro de los corchetes, de esta manera deberemos utilizar parametros.
## nombre_completo = "Mr. {nombre} {primer_apellido} {segundo_apellido}".format(nombre= nombre,primer_apellido = apellido, segundo_apellido = 'Perez')

# FStrings - nos permiten generar nuevos strings apartir de otros utilizando interpolacion.
# la sintaxis para los fstrings es colocar una f antes de un string vacio y dentro colocar las llaves para generar la interpolacion
# Las llaves dentro del fstring aceptan todo tipo de datos, incluyendo expresiones.

nombre_completo = f'Mr. {nombre} {apellido} {"Perez"} {13.1416} {15 * 3} {3 < 5}'

print(nombre_completo)