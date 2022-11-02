# Validar sub strings
# Busqueda dentro de strings

titulo_curso = 'Curso profesional de Python, donde aprenderemos las bases de Python'

# Metodo count() - recibe como argumento un string, en este caso el que deseamos encontrar dentro de un string. 
# Este metodo retornara la cantidad de coincidencias en el string.

## contador = titulo_curso.count('Python')
## print(contador)

# Palabra reservada in(), con esto podemos conocer si un string contiene la palabra, letras o caracteres que buscamos.

# Es recomendable estandarizar nuestra busqueda, convirtiendo todas las palabras dentro del string a minusculas o mayusculas.

## print('python' in titulo_curso.lower())

# Metodo startswith() - recibe como argumento el string el cual queremos conocer si existe al inicio de nuestro string base.

## print(titulo_curso.lower().startswith('curso'))

# Por el contrario, tambien contamos con el metodo endswith().
print(titulo_curso.lower().endswith('python'))
