def promedio_estudiante(calificaciones):
    if len(calificaciones)== 0 :
        return 0.0
    media = sum(calificaciones)/len(calificaciones)
    return media
#Lista de calificaciones
calificaciones = [85, 92, 78]

#Calcular el promedio
promedio = promedio_estudiante(calificaciones)
print(promedio)
