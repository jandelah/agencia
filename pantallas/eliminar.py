from bd.conexion import conectar

def eliminar_r_auto(id_auto):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM autos WHERE id = %s"
    cursor.execute(sql, (id_auto,))
    conexion.commit()
    cursor.close()
    conexion.close()
    
    return '''
    <h2>Registro eliminado</h2>
    <a href="/">← Regresar</a>
    '''