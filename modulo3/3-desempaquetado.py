# Desempaquetado de tuplas

# El primer valor es asignado a la primera variable al desempaquetar desde una tupla.
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# En caso de no conocer la cantidad de elementos dentro de la tupla, podemos ayudarnos del asterisco ( * ) para asignarlos a una variable (resto_numeros). 

## uno, dos, tres, cuatro, *resto_numeros = numeros

# En caso de querer omitir los valores podemos ayudarnos del asterisco y un guion bajo ( *_ ).

## uno, dos, tres, cuatro, *_, ocho, nueve = numeros

#  Adicional a eso, si queremos obtener los ultimos elementos de la tupla, podemos agregar variables para asignar estos elementos.

## uno, dos, tres, cuatro, *resto_omitidos, ocho, nueve = numeros

# Si queremos omitir solo ciertos elementos lo podemos ralizar con guion bajo ( _ )

uno, _, tres, _, _, seis, *resto, nueve = numeros

print(uno)
# print(dos)
print(tres)
# print(cuatro)
# print(resto_numeros)

# Omitimos los valores y podemos asignar a variables de derecha a izquierda.
# print(resto_omitidos)
# print(ocho)
print(resto)
print(nueve)
