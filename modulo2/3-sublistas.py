# Sublistas

# Las sublistas se crean a partir de una lista
# indicando un rango de indices entre corchetes
# Estos indices no se refieren a los elementos dentro de la lista
# se comportan como una referencia entre los elementos de la lista
# si deseamos incluir el primer elemento, nuestro rango debe ser [0:1]

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]
#              0         1         2        3       4       5      6

# [start:end] Se crea una sublista con los elementos dentro del rango
# [start:] Se crea una sublista con todoss los elementos despues del inicio
# [:end] Se crea una sublista con todos los elementos hasta el rango final

sub_lista = lista_cursos[0:5]


# Sublista con salto de elementos
# [start:end:skip]

sub_lista_skip = lista_cursos[0:5:3]
print(sub_lista_skip)

# Tips
# 1.- Start y end no son obligatorios podemos crear un rango sin ellos [:]
# 2.- Si creamos una sublista con saltos negativos de 1 obtendremos la lista invertida [::-1]