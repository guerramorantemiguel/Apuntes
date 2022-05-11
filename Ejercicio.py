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

def Moda(caracteristicas):
  moda_mates = count.(notas_mates)
  print("La moda de todas las notas de matemáticas es:{}".format(moda_mates))

def Rango(caracteristicas):
  print("El rango de las notas de matemáticas, escritura y lectura es:{}".format(valor_maximo - valor_minimo))

# Creación deñ dataset con números aleatorios

from random import*
file = open("datospeso.csv", "w")
file.write("peso")

for i in range(100):
  num = randint(100,200)
  file.write("\n{}".format(num))
# En la línea 60 ponemos "datospeso.csv" porque el dataset se llama así


# desviacion tipica y varianza 
class Desviacion_tipica:
  def __init__(self, csv, columna):
    self.csv = csv
    self.columna = columna
  def calculo(self):
    desv = self.csv[self.columna].mad()
    print("La desviacion tipica es: ")
    print(desv)
class varianza:
  def __init__(self, csv, columna):
    self.csv = csv
    self.columna = columna
  def calculo(self):
    var = self.csv[self.columna].var()
    print("La varianza es :")
    print(var)

# Para hacer gráfico
import matplotlib.pyplot as plt
class Grafico():
  def __init__(self, lista, media, mediana):
    self.lista = lista
    self.media = media
    self.mediana = mediana
  def visualizacion(self):
    plt.subplot(2, 2, 1)
    plt.hist(self.lista)
    plt.title("Histograma y media")
    plt.axvline(self.media, color = 'color', linestyle = 'dashed', linewidth = 1, label = str(self.mediana))
    plt.legend(loc='upper right')

    plt.subplot(2, 2, 2)
    plt.hist(self.lista)
    plt.title("Histograma y media")
    plt.axvline(self.media, color = 'green', linestyle = 'dashed', linewidth = 1, label = str(self.media))
    plt.legend(loc = 'upper right')

    plt.subplot(2, 2, 4)
    plt.hist(self.lista)
    plt.title("Diagrama de caja y bigotes")
    plt.show()
fig, ax = plt.subplots()

class Grafico_barras:
  def __init__(self, csv, columna):
    self.csv = csv
    self.columna = columna

  def crear_grafico(self):
    fig, ax = plt.subplots()
    self.csv[self.columna].plot(kind="hist", ax = ax)
    ax.set_title("histograma", loc = "center", fontdict = {'fontsize': 14, 'fontweight' : 'bold', 'color': 'tab:blue'})
    ax.set_ylabel('')
    plt.savefig('img/histograma-' + '-'.join(self.columna) + '.png', bbox_inches = 'tight')
    return
class Grafico_sectores:
  def __init__(self, csv, columna):
    self.csv = csv
    self.columna = columna
  def crear_grafico(self):
    fig, ax = plt.subplots()
    self.csv[self.columna].plot(kind="hist", ax = ax)
    ax.set_title("histograma", loc = "center", fontdict = {'fontsize': 14, 'fontweight' : 'bold', 'color': 'tab:blue'})
    ax.set_ylabel('')
    plt.savefig('img/histograma-' + '-'.join(self.columna) + '.png', bbox_inches = 'tight')
    return

class Grafico_histograma:
  def __init__(self, csv, columna):
    self.csv = csv
    self.columna = columna
  def crear_grafico(self):
    fig, ax = plt.subplots()
    self.csv[self.columna].plot(kind="hist", ax = ax)
    ax.set_title("histograma", loc = "center", fontdict = {'fontsize': 14, 'fontweight' : 'bold', 'color': 'tab:blue'})
    ax.set_ylabel('')
    plt.savefig('img/histograma-' + '-'.join(self.columna) + '.png', bbox_inches = 'tight')
    return
    

