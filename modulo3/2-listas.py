# Convertir tuplas a listas y biceversa.

# Esto es una lista
cursos = ["Python", "Django", "Flask"]

# Con la funcion tuple() es posible generar una tupla a partir de una lista.
cursos_tupla = tuple(cursos)

print(cursos_tupla)
print(type(cursos_tupla))

# Esto es una tupla
niveles = ('Básico', 'Intermedio', 'Avanzado')

# Con la funcion list() es posible generar una lista a partir de una tupla
niveles_lista = list(niveles)

print(niveles_lista)
print(type(niveles_lista))