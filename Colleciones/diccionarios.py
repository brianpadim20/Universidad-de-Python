# Está compuesto por una llave y un valor, no hay índices en un diccionario, para acceder se proporciona la llave

diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'

}

print(diccionario)

# Largo de los elementos del diccionario
print(len(diccionario))

# Acceder a un elemento en particular
print(diccionario['DBMS'])

# Otra forma de recuperar un elemento
print(diccionario.get('OOP'))

# Modificar elementos
diccionario['OOP']= 'Programación orientada a objetos'
print(diccionario)

# Recorrer los elementos de un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otra forma, para recuperar únicamente las llaves
for termino in diccionario.keys():
    print(termino)

# Si se quieren recuperar solamente los valores asociados a los términos
for valor in diccionario.values():
    print(valor)

# Comprobar existencia de algún elemento
print('IDE' in diccionario)

# Agregar un elemento en un diccionario
diccionario['PK']='Primary Key'
print(diccionario)

# Remover un elemento
diccionario.pop('OOP')
print (diccionario)

# Limpiar el diccionario:
diccionario.clear()
print (diccionario)

# Eliminar el diccionario
del diccionario
print(diccionario)