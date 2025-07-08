from bd.conexion import conectar

def buscarAuto(valor):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    SELECT * FROM autos 
    WHERE marca LIKE %s 
       OR color LIKE %s 
       OR id LIKE %s
    """
    valor_busqueda = f"%{valor}%"
    datos = (valor_busqueda, valor_busqueda, valor_busqueda)

    cursor.execute(sql, datos)
    resultado = cursor.fetchall()
    tabla = '''
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Marca</th>
                <th>Modelo</th>
                <th>Color</th>
                <th>Número de puertas</th>
                <th>Número de pasajeros</th>
            </tr>
        </thead>
        <tbody>
    '''
    for auto in resultado:
        tabla += f'''
            <tr>
                <td>{auto[0]}</td>
                <td>{auto[1]}</td>
                <td>{auto[2]}</td>
                <td>{auto[3]}</td>
                <td>{auto[4]}</td>
                <td>{auto[5]}</td>
            </tr>
        '''
    tabla += '''
        </tbody>
    </table>
    <br/><a href="/">← Volver al inicio</a>
    '''
    
    cursor.close()
    conexion.close()
    return tabla
