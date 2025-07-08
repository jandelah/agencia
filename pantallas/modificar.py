from bd.conexion import conectar

def modificar_auto_r(id_auto, request=None):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # al primer click, mostrar datos (request está vacío)
    if request is None:
        sql = "SELECT * FROM autos WHERE id = %s"
        cursor.execute(sql, (id_auto,))
        auto = cursor.fetchone()
        cursor.close()
        conexion.close()
        
        if auto is None:
            return '<h2>Error: Registro no encontrado</h2><a href="/">← Regresar</a>'
        
        return f'''
        <h1>Modificar Auto</h1>
        <form action="/modificar_auto/{id_auto}" method="POST">
            Marca: <input name="marca" value="{auto[1]}" required/><br/>
            Modelo: <input name="modelo" type="number" value="{auto[2]}" required/><br/>
            Color: <input name="color" value="{auto[3]}" required/><br/>
            Número de puertas: <input name="numero_puertas" type="number" value="{auto[4]}" required/><br/>
            Número de pasajeros: <input name="numero_pasajeros" type="number" value="{auto[5]}" required/><br/>
            <button type="submit">Guardar cambios</button>
        </form>
        <a href="/">← Volver al inicio</a>
        '''
    
    #Si hay algo en el request, modificar
    else:
        marca = request.form["marca"]
        modelo = request.form["modelo"]
        color = request.form["color"]
        numero_puertas = request.form["numero_puertas"]
        numero_pasajeros = request.form["numero_pasajeros"]
        
        sql = "UPDATE autos SET marca = %s, modelo = %s, color = %s, numero_puertas = %s, numero_pasajeros = %s WHERE id = %s"
        datos = (marca, modelo, color, numero_puertas, numero_pasajeros, id_auto)
        cursor.execute(sql, datos)
        conexion.commit()
        cursor.close()
        conexion.close()
        
        return '<h2>Los datos del auto se han modificado</h2><a href="/">← Regresar</a>'