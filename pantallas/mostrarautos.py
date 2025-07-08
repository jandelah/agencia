from bd.autobd import mostrar_autos

def pantalla_mostrar_autos():
    resultado = mostrar_autos()
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
                <td>
                    <a href="/modificar_auto/{auto[0]}" class="btn btn-modificar">Modificar</a>
                    <a href="/eliminar_auto/{auto[0]}" class="btn btn-eliminar" 
                       onclick="return confirm('¿Seguro de que deseas eliminar?')">Eliminar</a>
                </td>
            </tr>
        '''
    tabla += '''
        </tbody>
    </table>
    '''
    return tabla
