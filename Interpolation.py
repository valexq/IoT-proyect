import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import scipy
from scipy import interpolate

#Abro el archivo en el que voy a trabajar
#y creo las listas que voy a usar previamente para almacenar
archivo =  open("SCD30_CO2.txt", "r")
muestrastiempo = []
muestrasdato1 = []
muestrasdato2 = []
muestrasdato3 = []
interpolation1 = []
muestrasdato1inter = []

##Leo las lineas y guardo el primer timestamp de cada linea en una lista
for linea in archivo.readlines():   
    partes = linea.strip().split(' ')
    tiempo = partes[0]
    dato1 = partes[4]
    dato2 = partes[5]
    dato3 = partes[6]
    muestrastiempo.append(int(tiempo))
    muestrasdato1.append(dato1)     
    muestrasdato2.append(dato3)  
    muestrasdato3.append(dato3) 
archivo.close()

# Diferencias de tiempo
diferencias = np.diff(muestrastiempo)
##print(diferencias)
# Calcular la media de las diferencias de tiempos
media_diferencias = np.mean(diferencias)
#print("Media de las diferencias:", round(media_diferencias, 2))
# Calcular la desviación estandar de las diferencias de tiempo
desviacion_estandar = np.std(diferencias)
#print("Desviación estándar:",round(desviacion_estandar, 2) )

#Función para calcular la diferencia entre dos muestras 
def diferencia_tiempo(muestra1, muestra2):
    diferencia = muestra2 - muestra1
    return diferencia

##Gráficos de prueba para mostrar los datos solo en un rango de 1 a 100 números
tiempo1 = muestrastiempo[0:50]
datos1 = muestrasdato1[0:50]
#plt.plot(tiempo1 ,datos1 ) 
#plt.xlabel('Timestamps')
#plt.ylabel('Datos')
##plt.show()

#Condicional que valida si el timestamp es igual o mayor a la 
# media de todos los timestamps
#Si es así, entonces se hace la interpolación 

##Prueba de interpolación
#function = scipy.interpolate.interp1d(muestrastiempo, muestrasdato1)
#x_new = np.arange(21162, 188541368, 10711)
#y_new = function(x_new)

##plt.show()
#recorrer la lista de tiempo para comparar cada uno de los tiempos 
#el actual y el siguiente con la media de tiempo de todos los datos
#luego agregar el nuevo dato de interpolacion en la lista de timestamps y datos1
tiemponuevo = []
totaldif = 0
muestrasdato1inter = list(muestrasdato1)
nuevotiempo = list(muestrastiempo)
for i in range(len(muestrastiempo)-1):
    #for j in range(len(muestrasdato1)-1):
        muestra_actual = muestrastiempo[i]
        muestra_siguiente = muestrastiempo[i+1]
        diferencia = diferencia_tiempo(muestra_actual, muestra_siguiente)
        totaldif += diferencia
        media = totaldif/len(muestrastiempo)
        if (diferencia > media_diferencias):
            #Agregar el nuevo timestamp en la nueva interpolacion
            nuevo_timestamp = muestra_actual + 10711
            indice_insertar = i + 1
            nuevotiempo.insert(indice_insertar, nuevo_timestamp)
            #Funcion interpoladora
            function = interp1d(muestrastiempo, muestrasdato1)
            #Generar nuevos puntos
            x_new = np.arange(muestra_actual, muestra_siguiente, 10711)
            y_new = function(x_new)
            #print("\nDatos interpolados:")
            #print("x_new =", x_new)
            #print("y_new =", y_new)
            # llenar la nueva lista con los datos interpolados
            for j, valor_interpolado in enumerate(y_new):
                muestrasdato1inter.insert(i+j+1, str("{:.2f}".format(valor_interpolado)))
            ##plt.plot(x_new , y_new )
#print(muestrasdato1inter)
print(nuevotiempo)
print(len(nuevotiempo))
print(len(muestrasdato1inter))

datos_int = muestrasdato1inter[0:50]

plt.plot(tiempo1 , datos1) 
plt.xlabel('Timestamps')
plt.ylabel('Datos interpolados')
#plt.show()
# Crear una nueva lista en la que se registren los datos originales
# y los nuevos datos interpolados con el fin de graficar y ver la 
# correcion de los datos           
# luego pasar esos datos corregidos a un nuevo txt y borrar las listas creadas
# teniendo en cuenta que se debe agregar un nuevo timestamp en el dato interpolado
# junto con los demas datos interpolados



        
        #x_interp = np.linspace(24, 27, 17601)
        #interp_func1 = interp1d(np.array(muestrasdato1)[condicion(muestrastiempo)], kind='linear')
        #y_interp1 = interp_func1(x_interp)
        #print("Interpolación de la primera lista:")
        #print(y_interp1)    















    















