from flask import Flask, render_template
import backend 

app = Flask(__name__)

@app.route('/')
def index():
    alfabeto = backend.ALFABETO
    iteraciones = backend.ITERACIONES_KLEENE
    
    # Aquí se genera la lista de cadenas y los datos de crecimiento
    cadenas_lista = backend.kleene_star(alfabeto, iteraciones)
    crecimiento_datos = []
    
    for i in range(1, iteraciones + 1):
        res = backend.kleene_star(alfabeto, i)
        crecimiento_datos.append({"iter": i, "cant": len(res)})
    
    return render_template('index.html', 
                           alfabeto=alfabeto, 
                           iteraciones=iteraciones, 
                           cadenas=cadenas_lista,      
                           crecimiento=crecimiento_datos)

if __name__ == "__main__":
    app.run(debug=True)