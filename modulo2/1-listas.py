""" 
Todos los valores almacenados dentro de una lista les correspondera 
una posicion dentro de la lista, conocida como indice
y mediante esta posicion podemos obtener y actualizar
elementos dentro de la lista
"""
#                  0         1         2       3        4  
lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java"]
#                 -5        -4        -3       -2      -1

primer_curso = lista_cursos[2]
print(primer_curso)

# Las listas se leen de izquierda a derecha
# Pero si trabajamos con numeros negativos la leemos de derecha a izquierda

ultimo_curso = lista_cursos[-1]
print(ultimo_curso)

# Cuando intentemos acceder a un elemento cuyo indice no existe, obtendremos un error

# print(lista_cursos[25])
