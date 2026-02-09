"""
Programa para convertir números a binario y hexadecimal.
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
                        number = int(float(line))
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


def convert_to_binary(number):
    """Convierte un número decimal a binario usando algoritmo básico."""
    if number == 0:
        return "0"

    is_negative = number < 0
    number = abs(number)

    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    if is_negative:
        binary = "-" + binary

    return binary


def convert_to_hexadecimal(number):
    """Convierte un número decimal a hexadecimal usando algoritmo básico."""
    if number == 0:
        return "0"

    is_negative = number < 0
    number = abs(number)

    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""

    while number > 0:
        remainder = number % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        number = number // 16

    if is_negative:
        hexadecimal = "-" + hexadecimal

    return hexadecimal


def write_results_to_file(filename, conversions, elapsed_time):
    """Escribe los resultados de conversión en un archivo."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("RESULTADOS DE CONVERSIÓN DE NÚMEROS\n")
            file.write("=" * 70 + "\n\n")
            file.write(f"{'Decimal':<15} {'Binario':<30} {'Hexadecimal':<20}\n")
            file.write("-" * 70 + "\n")

            for conversion in conversions:
                decimal = conversion['decimal']
                binary = conversion['binary']
                hexadecimal = conversion['hexadecimal']
                file.write(f"{decimal:<15} {binary:<30} {hexadecimal:<20}\n")

            file.write("\n" + "=" * 70 + "\n")
            file.write(f"Total de números convertidos: {len(conversions)}\n")
            file.write(f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n")
    except (IOError, OSError) as e:
        print(f"Error al escribir el archivo de resultados: {e}")


def main():
    """Función principal del programa."""
    if len(sys.argv) < 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    print("Leyendo datos del archivo...")
    numbers = read_numbers_from_file(filename)

    if not numbers:
        print("Error: No se encontraron números válidos en el archivo.")
        sys.exit(1)

    print(f"Se leyeron {len(numbers)} números válidos.")
    print("\nConvirtiendo números...")

    # Convertir números
    conversions = []
    for number in numbers:
        binary = convert_to_binary(number)
        hexadecimal = convert_to_hexadecimal(number)
        conversions.append({
            'decimal': number,
            'binary': binary,
            'hexadecimal': hexadecimal
        })

    # Calcular tiempo transcurrido
    elapsed_time = time.time() - start_time

    # Mostrar resultados en consola
    print("\n" + "=" * 70)
    print("RESULTADOS DE CONVERSIÓN DE NÚMEROS")
    print("=" * 70)
    print(f"{'Decimal':<15} {'Binario':<30} {'Hexadecimal':<20}")
    print("-" * 70)

    for conversion in conversions:
        decimal = conversion['decimal']
        binary = conversion['binary']
        hexadecimal = conversion['hexadecimal']
        print(f"{decimal:<15} {binary:<30} {hexadecimal:<20}")

    print("\n" + "=" * 70)
    print(f"Total de números convertidos: {len(conversions)}")
    print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")

    # Escribir resultados en archivo
    output_file = "../results/ConvertionResults.txt"
    write_results_to_file(output_file, conversions, elapsed_time)
    print(f"\nResultados guardados en '{output_file}'")


if __name__ == "__main__":
    main()
