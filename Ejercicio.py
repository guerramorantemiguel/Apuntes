import pandas as pd

notas = pd.read_csv("NOMBRECSV.csv", header = 0)
lo que sea = list(notas["lo que ponga"])
lo que sea = list(notas["lo que ponga"])

m = len(notas_mates)

for i in range (1,m):
  diccionario = {"notas_mates":notas_mates, "notas_lectura":notas_lectura, "notas_escritura":notas_escritura}
  print(1)

print("— CANTIDAD DE OBSERVACIONES --") 
n = caracteristica.count() 
print("Cantidad de observaciones = " + str(n))

print ("VALORES MÁXIMOS")  
valor_maximo = caracteristica.sort_values()  
print("Valor máximo: " +  
str(valoresOrdenados[len(valoresOrdenados)-1])) 

for num in notas_mates:
  if num > valor_maximo or valor_maximo == None:
  print(valor_maximo)

print ("VALORES MÍNIMOS")  
valor_minimo = caracteristica.sort_values()    
print("Valor mínimo: "+str(valoresOrdenados [0])) 

for num in notas_mates:
  if num < valor_minimo or valor_minimo == None:
  print(valor_minimo)

# Para hacer el dataset
# Poner algo.csv
# dato;dato;dato
# Ejemplo: nombre;peso
# Ejemplo: Antonio;55

print("NOTAS MEDIAS") 
suma_de_las_notas_mates = sum(notas_mates)
media_notas_mates = suma_de_las_notas_mates/1
print("La nota media en mates es{}".format(media_notas_mates))

def Mediana(caracteristica):  
  mediana = int(1/2)
  mediana_mates = (notas_mates[mediana] + notas_mates[mediana + 1])/2
  print("La mediana de todas las notas de matemáticas es:{}".format(mediana_mates))