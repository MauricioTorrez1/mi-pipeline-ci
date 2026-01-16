## Un Unit Test (Prueba Unitaria) es un fragmento de código diseñado para verificar la funcionalidad de la parte más pequeña posible 
# de tu aplicación (una "unidad") de forma aislada. Un Unit Test NUNCA debe conectarse a sistemas reales. Se usan Mocks (falsificaciones). 
# Le dicen al test: "Simula que la base de datos respondió X, no te conectes de verdad.
import unittest
from funcion_calculadora import calcular_interes_compuesto

class TestFinanciero(unittest.TestCase):

    def test_calculo_basico(self):
        # Escenario: 100 pesos, 4% interes, 1 año. Deberia de dar 104.
        resultado = calcular_interes_compuesto(100, 4, 1)
        # self.assertEqual(a, b) Significa: "Afirmo que A es igual a B"
        self.assertEqual(resultado, 104.00)
    
    def test_calculo_dos_anios(self):
        # Escenario: 100 pesos, 10% interes, 2 años
        # Año 1: 110, Año 2: 121.
        resultado = calcular_interes_compuesto(100, 10, 2)
        self.assertEqual(resultado, 121.00)

if __name__ == '__main__':
    # unittest.main(): Esta función busca automáticamente dentro de tu clase todas las funciones que empiecen con la palabra mágica test_.
    # Una vez que las encuentra, las ejecuta una por una y te imprime el reporte final en la consola (cuántas pasaron y cuántas fallaron).
    unittest.main()

    