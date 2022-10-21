# Operadores logicos

'''
- Nos permiten comparar tipos booleanos, obtendremos (True o False)
 and - Todos valores deben ser verdaderos para dar verdadero
 or - Al menos un valor verdadero entregara verdadero
 not - Convierte True a False y False a True
'''

resultado = True and True
print(resultado)

resultado = False and True
print(resultado)

resultado = True and 10 > 20
print(resultado)

resultado = True or False
print(resultado)

# Podemos combinar operadores logicos utilizando parentesis
# para generar comparaciones mas complejas
resultado = False or (100 < 20)
print(resultado)

resultado = not False
print(resultado)
