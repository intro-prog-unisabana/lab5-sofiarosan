def promedio_estudiante(calificaciones):
    media = sum(calificaciones)/len(calificaciones)
    return media
#Lista de calificaciones
calificaciones = [85, 92, 78]

#Calcular el promedio
promedio = promedio_estudiante(calificaciones)
print(promedio)
