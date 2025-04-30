# Cree una aplicación web en Python utilizando Flask que reciba en la URL un número y renderice el factorial de ese número.
import math
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/factorial/<int:number>')
def factorial(number):
    if number < 0:
        return "El factorial no está definido para números negativos."
    else:
        result = math.factorial(number)
    
    return jsonify(f'factorial({number}) = {result}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    
    
# Para ejecutar la aplicación, guarda el código en un archivo llamado factorial.py y ejecuta el siguiente comando en la terminal:
