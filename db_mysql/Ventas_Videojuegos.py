import pandas as pd
import mysql.connector

# Cargar CSV
df = pd.read_csv('vgsales.csv')
df = df.dropna()  # Limpieza básica

# Conexión a la base de datos
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1193104127',
    database='videojuegos'
)
cursor = conn.cursor()

# Diccionarios para evitar duplicados
plataformas = {}
editores = {}
generos = {}

# Insertar datos normalizados
for _, row in df.iterrows():
    # Insertar plataforma
    plat = row['Platform']
    if plat not in plataformas:
        cursor.execute("INSERT INTO Plataforma (nombre) VALUES (%s)", (plat,))
        plataformas[plat] = cursor.lastrowid
    id_plat = plataformas[plat]

    # Insertar editor
    edit = row['Publisher']
    if edit not in editores:
        cursor.execute("INSERT INTO Editor (nombre) VALUES (%s)", (edit,))
        editores[edit] = cursor.lastrowid
    id_edit = editores[edit]

    # Insertar género
    gen = row['Genre']
    if gen not in generos:
        cursor.execute("INSERT INTO Genero (nombre) VALUES (%s)", (gen,))
        generos[gen] = cursor.lastrowid
    id_gen = generos[gen]

    # Insertar videojuego
    cursor.execute("""
        INSERT INTO Videojuego (nombre, anio, id_plataforma, id_editor, id_genero)
        VALUES (%s, %s, %s, %s, %s)
    """, (row['Name'], int(row['Year']), id_plat, id_edit, id_gen))
    id_juego = cursor.lastrowid

    # Insertar ventas
    cursor.execute("""
        INSERT INTO Venta (id_juego, na_sales, eu_sales, jp_sales, other_sales, global_sales)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (id_juego, row['NA_Sales'], row['EU_Sales'], row['JP_Sales'], row['Other_Sales'], row['Global_Sales']))

conn.commit()
cursor.close()
conn.close()
