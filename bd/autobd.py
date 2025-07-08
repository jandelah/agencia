from bd.conexion import conectar

def insertar_auto(a1):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO autos (marca, modelo, color, numero_puertas, numero_pasajeros) VALUES (%s, %s, %s, %s, %s)"
    datos = (
        a1.get_marca(),
        a1.get_modelo(),
        a1.get_color(),
        a1.get_numero_puertas(),
        a1.get_numero_pasajeros()
    )
    cursor.execute(sql, datos)
    conexion.commit()
    cursor.close()
    conexion.close()

def mostrar_autos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM autos")
    resultado = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultado
