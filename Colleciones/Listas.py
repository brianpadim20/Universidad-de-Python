nombres = ["Brian", "Andrés", "José", "Andrea", "Karla"]

print(nombres)

print (nombres[0:2])
print (nombres[:3])#Accede a los elementos de la lista, sin incluír el # 3
print (nombres[1:])#No incluye el primer índice

nombres[3]="Lorena"

#Acceder a los elementos
for i in nombres:
    print (i)
else:
    print("No hay mas nombres en la lista")

# Longitud de la list:
print(len(nombres))

# Agregar un elemento a la lista:
nombres.append("Carolina")
print(nombres)

#Insertar un elemento en un índice específico:
nombres.insert(2, "Michael")
print(nombres)

# Remover un elemento
nombres.remove("Michael")
print(nombres)

# Remover el últimno valor agregado:
nombres.pop()
print (nombres)

# Eliminar un elemento en un índice indicado
del nombres[1]
print(nombres)

# Limpiar todos los elementos de la lista
nombres.clear()
print(nombres)

# Borrar la lista por completo
del nombres
print (nombres)