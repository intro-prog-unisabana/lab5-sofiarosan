def promedio_estudiante(calificaciones):
    return sum(calificaciones)/len(calificaciones)

calificaciones = []
while True:
    calificacion =input()
    if calificacion.isdecimal():
        calificaciones.append(float(calificacion))
    else:
        break

promedio = promedio_estudiante(calificaciones)
print(promedio)