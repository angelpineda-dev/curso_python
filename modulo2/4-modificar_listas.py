# Modificar listas

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]
lista_cursos_2 = ["C", "C++", "Docker"]
# Para conocer la longitud de una lista, podemos hacer uso de la funcion len()
print(len(lista_cursos))

# El metodo append agrega elementos al final de la lista.
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('JavaScript')

# Insertar elementos en un indice especifico con el metodo insert()
# Este recibe 2 argumentos, el indice y el elemento.

lista_cursos.insert(3, 'Rails')
lista_cursos.insert(0, 'PyGame')

# Extender una lista - Podemos hacer mas grande nuestra lista apartir de otra.
lista_cursos.extend(lista_cursos_2)

# Eliminar elementos de la lista con el metodo remove()
# Recibe como argumento el elemento a remover.
print(lista_cursos)
lista_cursos.remove('Flask')
print(lista_cursos)

# Eliminar elementos mediante los indices con la palabra reservada del
del lista_cursos[0]
print(lista_cursos)

# Eliminar todos los elementos de una lista con el metodo clear()
lista_cursos.clear()
print(lista_cursos)