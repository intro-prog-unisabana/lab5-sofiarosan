def list_shift (datos, valor):
    for i in range(len(datos)):
        datos[i]= datos[i]+valor

#Funcion de promedio
def calc_avg(i):
    media= sum(i)/len(i)
    return media
datos =[2.0, 4.0, 6.0, 8.0]

prom = calc_avg (datos)

list_shift (datos, -prom)

def print_normalized(datos):
    print (datos)

print_normalized(datos)