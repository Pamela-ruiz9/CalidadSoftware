"""
Script para ejecutar todos los casos de prueba.

Automatiza la ejecución de todos los casos de prueba y verifica los resultados.
"""

import subprocess
import sys

# Casos de prueba esperados
TEST_CASES = [
    {
        'name': 'TC1',
        'products': 'tests/TC1/TC1.ProductList.json',
        'sales': 'tests/TC1/TC1.Sales.json',
        'expected': 2481.86
    },
    {
        'name': 'TC2',
        'products': 'tests/TC2/TC2.ProductList.json',
        'sales': 'tests/TC2/TC2.Sales.json',
        'expected': 166568.23
    },
    {
        'name': 'TC3',
        'products': 'tests/TC3/TC3.ProductList.json',
        'sales': 'tests/TC3/TC3.Sales.json',
        'expected': 165235.37
    }
]


def run_test(test_case):
    """Ejecutar un caso de prueba."""
    cmd = [
        sys.executable,
        'source/computeSales.py',
        test_case['products'],
        test_case['sales']
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()

    # Extraer el número total (última línea)
    lines = output.split('\n')
    total = float(lines[-1])

    return total


def main():
    """Ejecutar todos los casos de prueba."""
    print("=" * 60)
    print("EJECUTANDO CASOS DE PRUEBA")
    print("=" * 60)
    print()

    passed = 0
    failed = 0

    for test in TEST_CASES:
        print(f"Ejecutando {test['name']}...", end=' ')
        try:
            result = run_test(test)
            if abs(result - test['expected']) < 0.01:
                print(f"✓ PASÓ (esperado: {test['expected']}, "
                      f"obtenido: {result})")
                passed += 1
            else:
                print(f"✗ FALLÓ (esperado: {test['expected']}, "
                      f"obtenido: {result})")
                failed += 1
        except Exception as e:
            print(f"✗ ERROR: {e}")
            failed += 1

    print()
    print("=" * 60)
    print(f"RESUMEN: {passed} pasados, {failed} fallidos de "
          f"{len(TEST_CASES)} totales")
    print("=" * 60)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
