from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Holadesde mi servidor'

@app.route('/saludo/<persona>')
def saludosDinamico(persona):
    return 'Hola %s, bienvenido!!!' % persona
@app.route('/cuadrado/<init:num>')
def calculaCuadrado(num):
    resp = num * num
    return 'Respuesta: %f' %resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
