from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario_notas')
def formulario_notas():
    return render_template('formulario_notas.html')

@app.route('/procesar_ejercicio1', methods=['POST'])
def procesar_ejercicio1():
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    promedio = (nota1 + nota2 + nota3) / 3
    estado = 'Aprobado' if (promedio >= 40 and asistencia >= 75) else 'Reprobado'

    return f'Promedio: {promedio}, Estado: {estado}'

@app.route('/formulario_nombres')
def formulario_nombres():
    return render_template('formulario_nombres.html')

@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    nombres = [nombre1, nombre2, nombre3]
    nombre_largo = max(nombres, key=len)
    longitud = len(nombre_largo)

    return f'El nombre con mayor cantidad de caracteres es: {nombre_largo}, Tiene: {longitud} caracteres'

if __name__ == '__main__':
    app.run(debug=True)



