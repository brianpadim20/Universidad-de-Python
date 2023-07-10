# No se sabe la cantidad de argumentos (parámetros) que se le dará a la función

def listarNombres(*nombres): #El * significa que no se sabe la cantidad de parámetros y se tomará como una tupla
    for nombre in nombres:
        print(nombre)

listarNombres('Brian', 'Andrés', 'Patiño', 'Sánchez')