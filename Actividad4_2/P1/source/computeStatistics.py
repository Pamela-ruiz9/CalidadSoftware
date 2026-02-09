"""
Programa para calcular estadísticas descriptivas de un archivo de números.
Cumple con el estándar PEP-8.
"""

import sys
import time


def read_numbers_from_file(filename):
    """
    Lee números de un archivo y los retorna como lista.
    Maneja errores de datos inválidos.
    """
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:
                    try:
                        number = float(line)
                        numbers.append(number)
                    except ValueError:
                        print(f"Error en línea {line_num}: '{line}' "
                              f"no es un número válido. Se omite.")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no fue encontrado.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: No hay permisos para leer '{filename}'.")
        sys.exit(1)
    except (IOError, OSError) as e:
        print(f"Error inesperado al leer el archivo: {e}")
        sys.exit(1)

    return numbers


def calculate_mean(numbers):
    """Calcula la media de una lista de números."""
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def calculate_median(numbers):
    """Calcula la mediana de una lista de números."""
    if not numbers:
        return 0

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]

    return median


def calculate_mode(numbers):
    """Calcula la moda de una lista de números."""
    if not numbers:
        return []

    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_frequency = 0
    for freq in frequency.values():
        max_frequency = max(max_frequency, freq)

    modes = []
    for num, freq in frequency.items():
        if freq == max_frequency:
            modes.append(num)

    return modes


def calculate_variance(numbers, mean):
    """Calcula la varianza de una lista de números."""
    if not numbers:
        return 0

    sum_squared_diff = 0
    for num in numbers:
        diff = num - mean
        sum_squared_diff += diff * diff

    return sum_squared_diff / len(numbers)


def calculate_standard_deviation(variance):
    """Calcula la desviación estándar a partir de la varianza."""
    if variance < 0:
        return 0

    # Implementación del algoritmo de Newton para calcular raíz cuadrada
    if variance == 0:
        return 0

    x = variance
    epsilon = 0.00000001

    while True:
        root = 0.5 * (x + (variance / x))
        if abs(root - x) < epsilon:
            break
        x = root

    return root


def write_results_to_file(filename, results, elapsed_time):
    """Escribe los resultados en un archivo."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("RESULTADOS DE ESTADÍSTICAS DESCRIPTIVAS\n")
            file.write("=" * 50 + "\n\n")
            file.write(f"Cantidad de números: {results['count']}\n")
            file.write(f"Media: {results['mean']:.4f}\n")
            file.write(f"Mediana: {results['median']:.4f}\n")
            file.write(f"Moda: {results['mode']}\n")
            file.write(f"Varianza: {results['variance']:.4f}\n")
            file.write(f"Desviación estándar: {results['std_dev']:.4f}\n")
            file.write(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos\n")
    except (IOError, OSError) as e:
        print(f"Error al escribir el archivo de resultados: {e}")


def main():
    """Función principal del programa."""
    if len(sys.argv) < 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    print("Leyendo datos del archivo...")
    numbers = read_numbers_from_file(filename)

    if not numbers:
        print("Error: No se encontraron números válidos en el archivo.")
        sys.exit(1)

    print(f"Se leyeron {len(numbers)} números válidos.")
    print("\nCalculando estadísticas...")

    # Calcular estadísticas
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_standard_deviation(variance)

    # Preparar resultados
    results = {
        'count': len(numbers),
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        'std_dev': std_dev
    }

    # Calcular tiempo transcurrido
    elapsed_time = time.time() - start_time

    # Mostrar resultados en consola
    print("\n" + "=" * 50)
    print("RESULTADOS DE ESTADÍSTICAS DESCRIPTIVAS")
    print("=" * 50)
    print(f"Cantidad de números: {results['count']}")
    print(f"Media: {results['mean']:.4f}")
    print(f"Mediana: {results['median']:.4f}")
    print(f"Moda: {results['mode']}")
    print(f"Varianza: {results['variance']:.4f}")
    print(f"Desviación estándar: {results['std_dev']:.4f}")
    print(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos")

    # Escribir resultados en archivo
    output_file = "../results/StatisticsResults.txt"
    write_results_to_file(output_file, results, elapsed_time)
    print(f"\nResultados guardados en '{output_file}'")


if __name__ == "__main__":
    main()
