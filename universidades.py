#1. importo pandas
import pandas as pd

#2. traigo la fuente de datos
edadesCasa1 = [23,24,25,25,28]
edadesCasa2 = [1,4,24,26,70]


#3. genero los dataframe
dataFrame1 = pd.DataFrame(edadesCasa1)
dataFrame2 = pd.DataFrame(edadesCasa2)


#4. análisis descriptivo de los datos
analisis1 = dataFrame1.describe()
analisis2 = dataFrame2.describe()

#5. mostrar resultados
print(analisis1)
print("\n")
print(analisis2)

print("\n")

#actividad: (pacientes: Análisis de glucosa)
paciente1 = [45,280,124,250,79,300,26,59,200,60,210,39,110,59,69,54]
paciente2 = [120,125,122,125,119,121,120,119,120,124,125,120,117,130,127,125]

df1 = pd.DataFrame(paciente1)
df2 = pd.DataFrame(paciente2)

analisisD1 = df1.describe()
analisisD2 = df2.describe()

print(analisisD1)
print("\n")
print(analisisD2)


"""
paciente 1:
El promedio de glucosa es 122.75. Muy bajo según estimaciones médicas, pues el promedio normal está entre 140 y 199
la desviación estándar es 93.12, lo cual indica que los datos arrojados diariamente son alarmantemente variados.
El máximo que llegó a experimentar el paciente fue 300, un nivel de glucosa preocupante. Por otro lado, lo mismo se 
observa en el mínimo, 26, es igualmente alarmante.

paciente 2:
El promedio de glucosa es 122.43. Muy bajo según estimaciones médicas, pues el promedio normal está entre 140 y 199.
La desviación estándar es 3.52. No se observan cambios bruscos en los informes de glucosa diarios.
El máximo que llegó a experimentar el paciene fue 130, un valor muy bajo con respecto al promedio.
En el mínimo arrojó 117, un valor igualmente bajo de glucosa.


conclusiones: El paciente 1 experimentó un nivel altísimo de glucosa 
"""


"""
bd = pd.read_csv("./exterior.csv")





values_ = bd.columns.values
print(values_)

print("\n")
print("\n")


head = bd.head()
print(head)

print("\n")

tail = bd.tail(2)
print(tail)

print("\n")

cantidadPersonas = bd[["Edad (años)","Cantidad de personas"]].iloc[5]
print(cantidadPersonas)

"""