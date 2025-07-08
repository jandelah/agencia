from flask import Flask, request
from pantallas.mostrarautos import pantalla_mostrar_autos
from pantallas.nuevoauto import nuevo_auto
from pantallas.procesarnuevoauto import procesar_nuevo_auto
from pantallas.buscar import buscarAuto

app = Flask(__name__)

@app.route("/")
def inicio():
    
    return '''  <input name="valor" placeholder="Buscar auto" required />
  <button type="submit">Buscar</button>'''+mostrar_autos()+'''
    <form action="/nuevo_auto" method="get">
        <button type="submit">Agregar Nuevo Auto</button>
    </form>
    <form action="/buscar" method="post">
    <br/><a href="/">← Volver al inicio</a>
</form>

    '''

@app.route("/mostrarautos")
def mostrar_autos():
    return pantalla_mostrar_autos()

@app.route("/nuevoauto")
def nuevo_auto_formulario():
    return nuevo_auto()

@app.route("/buscar", methods=["POST"])
def buscar():
    valor = request.form["valor"]
    resultados = buscarAuto(valor)
    return resultados

@app.route("/procesarnuevoauto", methods=["POST"])
def guardar_nuevo_auto():
    respuesta = procesar_nuevo_auto(request)
    return respuesta

@app.route("/eliminar/<int:id_auto>")
def eliminar(id_auto):
    return eliminar_r_auto(id_auto)


@app.route("/modificar/<int:id_auto>", methods=["GET", "POST"])
def modificar(id_auto):
    if request.method == "GET":
        return modificar_auto_r(id_auto)
    else:
        return modificar_auto_r(id_auto, request)
if __name__ == "__main__":
    app.run(debug=True)
