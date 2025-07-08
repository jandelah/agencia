def nuevo_auto():
    return '''
    <html>
    <head>
    <style>
        /* Quitar flechitas de inputs numéricos */
        input[type=number]::-webkit-inner-spin-button,
        input[type=number]::-webkit-outer-spin-button {
            -webkit-appearance: none;
        }
        input[type=number] {
            -moz-appearance: textfield;
        }
    </style>
    </head>
    <body>
    <h1>Agregar un nuevo auto</h1>
    <form action="/procesar_nuevo_auto" method="POST">
        <input name="marca" placeholder="Marca" required/><br/>
        <input name="modelo" type="number" placeholder="Modelo" required/><br/>
        <input name="color" placeholder="Color" required/><br/>
        <input name="numero_puertas" type="number" placeholder="Número de puertas" required/><br/>
        <input name="numero_pasajeros" type="number" placeholder="Número de pasajeros" required/><br/>
        <button type="submit">Guardar auto</button>
    </form>
    </body>
    </html>
    '''
