import sqlite3
import csv

conector = sqlite3.connect('./assets/db/datos.db')
cursor = conector.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS usuarios(
        id TEXT PRIMARY KEY,
        permiso INTEGER,
        contrasena TEXT
    )
    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS ropa(
        id TEXT PRIMARY KEY,
        talle TEXT,
        genero TEXT,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL DEFAULT 0,
        descripcion TEXT NOT NULL
    );
    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS accesorios(
        id TEXT PRIMARY KEY,
        material TEXT,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL DEFAULT 0,
        descripcion TEXT NOT NULL
    );
    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS ventas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT,
        descripcion TEXT,
        cantidad INTEGER,
        precio REAL,
        descuento INTEGER,
        fecha TEXT,
        id_usuario TEXT,
        FOREIGN KEY (id_usuario) REFERENCES usuarios
    );
    '''
)

def agregar_stock_ropa(codigo, talle, genero, precio, stock, descripcion):
    datos = (codigo,talle,genero,precio,stock,descripcion)
    sql = """
    INSERT INTO ropa(id, talle, genero, precio, stock, descripcion)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, datos)
    conector.commit()

def agregar_stock_accesorio(codigo, material, precio, stock, descripcion):
    datos = (codigo,material,precio,stock,descripcion)
    sql = """
    INSERT INTO accesorios(id, material, precio, stock, descripcion)
    VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(sql, datos)
    conector.commit()

def agregar_ventas(codigo, descripcion, cantidad, precio, descuento, fecha, id_usuario):
    datos = (codigo, descripcion, cantidad, precio, descuento, fecha, id_usuario)
    sql = """
    INSERT INTO ventas(codigo, descripcion, cantidad, precio, descuento, fecha, id_usuario)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql, datos)
    conector.commit()

def agregar_usuario(nombre, contrasena, permiso):
    datos = (nombre, contrasena, permiso)
    sql = """
    INSERT INTO usuarios(id, contrasena, permiso)
    VALUES (?, ?, ?)
    """
    cursor.execute(sql, datos)
    conector.commit()
    return True

def eliminar(codigo, tabla):
    """
        Elimina con referencia de id
    """
    
    sql = f"DELETE FROM {tabla} WHERE id = '{codigo}'"
    cursor.execute(sql)
    conector.commit()

def actualizar_usuario(codigo, permiso, contrasena):
    sql = f"update usuarios set permiso = {permiso}, contrasena = '{contrasena}' WHERE id = '{codigo}'"
    cursor.execute(sql)
    conector.commit()

def actualizar_ropa(codigo, talle = "", genero = "", precio = "", stock = "", descripcion = ""):
    sql = "update ropa set "
    datos = []
    if talle != "" :
        sql += f"talle = ? "
        datos.append(talle)
    if genero != "" :
        sql += ", genero = ?"
        datos.append(genero)
    if precio != "":
        sql += ", precio = ?"
        datos.append(precio)
    if stock != "":
        sql += f"{"," if sql[-1] == "?" else ""} stock = ?"
        datos.append(stock)
    if descripcion != "":
        sql += ", descripcion = ? "
        datos.append(descripcion)
    sql += f"WHERE id = ?"
    datos.append(codigo)
    
    cursor.execute(sql,datos)
    conector.commit()

def actualizar_accesorios(codigo, material = "", precio = "", stock = "", descripcion = ""):
    sql = "update accesorios set "
    datos = []
    if material != "" :
        sql += f"material = ? "
        datos.append(material)
    if precio != "":
        sql += ", precio = ?"
        datos.append(precio)
    if stock != "":
        sql += ", stock = ?"
        datos.append(stock)
    if descripcion != "":
        sql += ", descripcion = ? "
        datos.append(descripcion)
    sql += f"WHERE id = ?"
    datos.append(codigo)
    
    cursor.execute(sql,datos)
    conector.commit()

def importar_datos_csv(ruta):
    with open(ruta, newline="", encoding="utf-8") as archivo:
            info = csv.DictReader(archivo)
            for linea in info:
                codigo = linea.get("Codigo")
                precio = linea.get("Precio")
                stock = linea.get("Stock")
                descripcion = linea.get("Descripcion")
                if "Talle" in linea.keys():
                    talle = linea.get("Talle")
                    genero = linea.get("Genero")
                    agregar_stock_ropa(codigo, talle, genero, precio, stock, descripcion)
                elif "Material" in linea.keys():
                    material = linea.get("Material")
                    agregar_stock_accesorio(codigo, material, precio, stock, descripcion)

def datos(tabla) -> list:
    sql = f'SELECT * FROM {tabla}'
    cursor.execute(sql)
    info = cursor.fetchall()
    return info

def busqueda_id(tabla,id) -> tuple:
    sql = f"SELECT * FROM {tabla} WHERE id = '{id}'"
    cursor.execute(sql)
    info = cursor.fetchone()
    return info

def busqueda_texto(tabla, texto):
    sql = f"SELECT * FROM {tabla} WHERE descripcion LIKE '%{texto}%'"
    cursor.execute(sql)
    info = cursor.fetchall()
    return info
    

def exportar_ventas_csv(ruta):
    sql = f"SELECT * FROM ventas"
    cursor.execute(sql)
    info = cursor.fetchall()
    
    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
        titulos = ["Codigo", "Descripcion","Cantidad", "Precio", "Descuento", "Fecha", "Vendedor"]
        escribir = csv.DictWriter(archivo, titulos)
        escribir.writeheader()
        
        for linea in info:
            nueva_lista = dict()
            nueva_lista["Codigo"] = linea[1]
            nueva_lista["Descripcion"] = linea[2]
            nueva_lista["Cantidad"] = linea[3]
            nueva_lista["Precio"] = linea[4]
            nueva_lista["Descuento"] = linea[5]
            nueva_lista["Fecha"] = linea[6]
            nueva_lista["Vendedor"] = linea[7]

            escribir.writerow(nueva_lista)


def generar_codigo():
    ropa = datos("ropa")
    accesorios = datos("accesorios")
    codigo = "000"
    if int(ropa[-1][0]) > int(accesorios[-1][0]):
        codigo += str(int(ropa[-1][0]) + 1)
    else:
        codigo += str(int(accesorios[-1][0]) + 1)
    
    return codigo[-3:]

if __name__ == "__main__":
    print(busqueda_id("usuarios","Ana"))