def promedio_estudiante(calificaciones):
    media = sum(calificaciones)/len(calificaciones)
    return media

calificaciones = []
while True:
    calificacion =input()
    if calificacion.isdecimal():
        calificaciones.append(float(calificacion))
    else:
        break

promedio = promedio_estudiante(calificaciones)
print(promedio)