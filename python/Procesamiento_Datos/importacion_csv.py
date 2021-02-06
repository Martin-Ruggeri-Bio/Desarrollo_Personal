import pandas as pd


url = '/home/martin/Descargas/train.csv'

df = pd.read_csv(url)

print(df.head())
# print(df.tail())

cabecera = ["ID", "Sobrevivió", "Clase", "Nombre", "Sexo", "edad", "Hermanos",
            "Hijos", "Ticket", "Tarifa", "Cabina", "Embarque"]
df.columns = cabecera
print(df.head())

ruta = '/home/martin/Descargas/titanic.csv'
df.to_csv(ruta)

print(df.dtypes)
print(df.describe())
print(df.describe(include="all"))
print(df.info)
print(df.dropna(subset=["Cabina"], axis=0))
print(df.dropna(axis=0))
print(df.dropna(axis=1))
print(df.dropna(subset=["Cabina"], axis=0, inplace=True))
print(pd.get_dummies(df, columns=["Sexo"], drop_first=True))
bins = [0, 5, 10, 20, 50, 75, 100]
name = [1, 2, 3, 4, 5, 6]
df["edad"] = pd.cut(df["edad"], bins, labels=name)
print(df["edad"])
print(df.head())
