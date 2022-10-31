# Strings - Strings con listados

## lenguajes = 'Python//Ruby//Java//Rust//C++//C'

# Metodo Split - Nos permite generar una lista a partir de un String.
# - Por defecto la separacion se realiza por los espacios encontrados en el String
# El metodo split recibe como argumento los caracteres a partir de los cuales queremos dividir el String
# - Adicionalmente el metodo Split recibe un segundo argumento que le indica la cantidad de divisiones que queremos

## listado_lenguajes = lenguajes.split('//',3) 
## print(listado_lenguajes)

# Metodo Join - Nos permite generar un String a partir de una lista.
# Para crear un String a traves del metodo join(),
# debemos crear un string con el caracter que deseamos una nuestros elementos del listado,
# normalmente es un string con un espacio
lenguajes = ['Python', 'Ruby','Java', 'Rust']

string_lenguajes = ' - '.join(lenguajes)
print(string_lenguajes)
print(type(string_lenguajes))


