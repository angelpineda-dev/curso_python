# Metodos listas.

lista = [8, 90, 1, 5, 44, 132, 60, 3, 4]

# Ordena los elementos del menor al mayor
lista.sort()
print(lista)

# Para ordenar la lista de manera inversa, podemos agregar el parametro reverse
lista.sort(reverse=True)
print(lista)

# Conocer el menor valor o el mayor
print(min(lista))
print(max(lista))

# Metodo para conocer si un elemento se encuentra dentro de la lista.
print(10 in lista)

# Para conocer si el elemento NO se encuentra dentro de la lista podemos utilizar el operador logico NOT
print(11 not in lista)