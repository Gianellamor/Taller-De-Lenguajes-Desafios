Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros

import math

def calculadora():
    numero = int(input('Número: '))
    funcion = input('Función (sin, cos, tan, exp, log): ').strip().lower()
    
    # Mapeo seguro de nombres a funciones de la librería math
    operaciones = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'exp': math.exp,
        'log': math.log
    }
    
    if funcion in operaciones:
        print(f"\nTabla de {funcion.upper()} del 1 al {numero}:")
        print("-" * 25)
        for i in range(1, numero + 1):
            resultado = operaciones[funcion](i)
            print(f"{i:<4} = {resultado:.6f}")
    else:
        print("Función no válida. Elegí entre: sin, cos, tan, exp, log")

calculadora()
