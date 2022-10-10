import pandas as pd
import os
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true' 
def listaPeliculas(rutaFileCsv: str) -> str: 
    direccion, extension= os.path.splitext(rutaFileCsv)
    if extension == ".csv?raw=true":
        try:
            datos= pd.read_csv(rutaFileCsv)
            datos= datos.drop(["Title", "Genres", "Content Rating", "Duration", "Aspect Ratio", "Year",
            "Budget", "Director", "Actor 1", "Actor 2", "Actor 3", "Facebook Likes - Director", "User Votes", 
            "Reviews by Users", "Facebook likes - Movie", "Facenumber in posters", "Reviews by Crtiics", 
            "IMDB Score", "Facebook Likes - Actor 2", "Facebook Likes - Actor 3", "Facebook Likes - cast Total",
            "Facebook Likes - Actor 1","Unnamed: 0"],axis=1)
            datos=pd.pivot_table(datos, index=("Country","Language"))
            return datos.head(10)
        except:
            print("Error al leer el archivo de datos.")
    else:
        print("Extensión inválida")
    return

print(listaPeliculas(rutaFileCsv))