# Un set no mantiene un orden ni permite almacenar elementos duplicados, no es posible modificar los 
# elementos almacenados en un set, pero si es posible agregar mas elementos o eliminarlos
# no tiene índices, por esto el orden es completamente aleatorio

planetas = {'Mercurio', 'Venus', 'Tierra','Marte'}
print (planetas)

# Largo de los elementos
print(len(planetas))

# Revisar si un elementos está definido en el set
print('Marte' in planetas)

# Agregar mas elementos
planetas.add('Jupiter')
print(planetas)

# Elemento duplicado
planetas.add('Jupiter')
print(planetas)

# Eliminar elementos posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)

# Si una llave no está en el set, mandará un key error, para que no lance error se usa la función discard:
planetas.discard('Tierras')
print(planetas)

# Eliminar todos los elemntos de un set:
planetas.clear()
print(planetas)

# Eliminar por completo el set
del planetas
print (planetas) # Arrojará un error