# Script de Python, pero lo escribiremos como una Función (def).
# Esto permite que GitHub Actions pueda usarla pasando parámetros automáticamente.

# Sintaxis de una función def nombredelafuncion (variables)
def calcular_interes_compuesto (capital, interes, años):
    """
    Docstring for calcular_interes_compuesto
    
    :param capital: inversión inicial
    :param interes: porcentaje de interes
    :param años: años de inversión
    """
    monto_final = capital * (1 + interes / 100) ** años 
    
    # Salida de la función (def)
    return round(monto_final, 2)

# Significa: "Ejecuta el código de abajo SOLO si soy yo el archivo principal que estás corriendo, 
# NO si alguien me está importando".
if __name__ == "__main__":
    print("----------Calculadora Manual -------")
    c = float(input("Ingresa el capital inicial a invertir: "))
    i = float(input("Ingresa la tasa de intéres anual: "))
    a = int(input("Ingresa la cantidad de años a invertir: "))
    resultado = calcular_interes_compuesto(c, i, a)
    print(f"Resultado : {resultado}")