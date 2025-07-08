from clases.auto import Auto
from bd.autobd import insertar_auto

def procesar_nuevo_auto(request):
    marca = request.form["marca"]
    color = request.form["color"]

    try:
        modelo = int(request.form["modelo"])
        numero_puertas = int(request.form["numero_puertas"])
        numero_pasajeros = int(request.form["numero_pasajeros"])
    except ValueError:
        return '''
        <h2>Error: Todos los campos numéricos deben contener solo números.</h2>
        <a href="/nuevo_auto">← Volver al formulario</a>
        '''

    a1 = Auto(marca, modelo, color, numero_puertas, numero_pasajeros)
    insertar_auto(a1)
    return '''
    <h2>Auto guardado correctamente</h2>
    <a href="/">← Volver al inicio</a>
    '''
