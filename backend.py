import math

ALFABETO = ['a', 'b'] 
ITERACIONES_KLEENE = 7 

def generar_cadenas(alfabeto, n):
    """1. Generación de cadenas hasta longitud n"""
    resultado = [""]
    for _ in range(n):
        nuevas = []
        for cadena in resultado:
            for simbolo in alfabeto:
                nuevas.append(cadena + simbolo)
        resultado.extend(nuevas)
    return list(dict.fromkeys(resultado))

def pertenece(cadena, lenguaje):
    """2. Pertenencia"""
    return cadena in lenguaje

def union(l1, l2):
    """3. Unión"""
    return list(set(l1) | set(l2))

def concatenacion(l1, l2):
    """4. Concatenación"""
    return [str(x) + str(y) for x in l1 for y in l2]

def kleene_star(L, max_iter):
    """5. Clausura de Kleene (L*)"""
    resultado = {""}
    actual = {""}
    for _ in range(max_iter):
        nuevo = {str(x) + str(y) for x in actual for y in L}
        resultado.update(nuevo)
        actual = nuevo
    return sorted(list(resultado), key=len)

def kleene_plus(L, max_iter):
    """6. Kleene Plus (L+)"""
    ks = kleene_star(L, max_iter)
    return [e for e in ks if e != ""]

def analizar_crecimiento(L, it):
    """7. Crecimiento"""
    for i in range(1, it + 1):
        res = kleene_star(L, i)
        print(f"Iteración {i}: {len(res)} cadenas")

# EJECUCIÓN TOTAL
if __name__ == "__main__":

    # 5. Ejecutar Kleene Star (El plato fuerte)
    todas_las_cadenas = kleene_star(ALFABETO, ITERACIONES_KLEENE)
    
    # Imprimir todas las cadenas
    print(todas_las_cadenas)
