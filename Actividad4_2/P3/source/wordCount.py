"""
Programa para contar la frecuencia de palabras en un archivo.
Cumple con el estándar PEP-8.
"""

import sys
import time


def read_words_from_file(filename):
    """
    Lee palabras de un archivo y las retorna como lista.
    Maneja errores de lectura.
    """
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Extraer palabras de la línea
                line_words = extract_words(line)
                words.extend(line_words)
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no fue encontrado.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: No hay permisos para leer '{filename}'.")
        sys.exit(1)
    except (IOError, OSError) as e:
        print(f"Error inesperado al leer el archivo: {e}")
        sys.exit(1)

    return words


def extract_words(text):
    """
    Extrae palabras de un texto separadas por espacios y
    caracteres especiales.
    """
    # Convertir a minúsculas para conteo case-insensitive
    text = text.lower()

    # Caracteres que se consideran separadores
    separators = " \t\n\r.,;:!?\"'()[]{}—-_/\\|<>@#$%^&*+=`~"

    # Reemplazar separadores por espacios
    for sep in separators:
        text = text.replace(sep, " ")

    # Dividir por espacios y filtrar vacíos
    words = []
    current_word = ""

    for char in text:
        if char == " ":
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    # Agregar última palabra si existe
    if current_word:
        words.append(current_word)

    return words


def count_word_frequency(words):
    """
    Cuenta la frecuencia de cada palabra en la lista.
    Retorna un diccionario con las palabras y sus frecuencias.
    """
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def sort_by_frequency(frequency_dict):
    """
    Ordena el diccionario de frecuencias de mayor a menor.
    Retorna una lista de tuplas (palabra, frecuencia).
    """
    # Convertir diccionario a lista de tuplas
    items = []
    for word, freq in frequency_dict.items():
        items.append((word, freq))

    # Ordenar usando bubble sort (algoritmo básico)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Ordenar por frecuencia descendente, luego alfabéticamente
            if (items[j][1] < items[j + 1][1] or
                    (items[j][1] == items[j + 1][1] and
                     items[j][0] > items[j + 1][0])):
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


def write_results_to_file(filename, sorted_frequency, total_words, elapsed_time):
    """Escribe los resultados del conteo de palabras en un archivo."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("RESULTADOS DE CONTEO DE PALABRAS\n")
            file.write("=" * 60 + "\n\n")
            file.write(f"{'Palabra':<30} {'Frecuencia':<15}\n")
            file.write("-" * 60 + "\n")

            for word, freq in sorted_frequency:
                file.write(f"{word:<30} {freq:<15}\n")

            file.write("\n" + "=" * 60 + "\n")
            file.write(f"Total de palabras: {total_words}\n")
            file.write(f"Palabras distintas: {len(sorted_frequency)}\n")
            file.write(f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n")
    except (IOError, OSError) as e:
        print(f"Error al escribir el archivo de resultados: {e}")


def main():
    """Función principal del programa."""
    if len(sys.argv) < 2:
        print("Uso: python wordCount.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    print("Leyendo palabras del archivo...")
    words = read_words_from_file(filename)

    if not words:
        print("Error: No se encontraron palabras válidas en el archivo.")
        sys.exit(1)

    print(f"Se leyeron {len(words)} palabras.")
    print("\nContando frecuencia de palabras...")

    # Contar frecuencia
    frequency = count_word_frequency(words)

    # Ordenar por frecuencia
    sorted_frequency = sort_by_frequency(frequency)

    # Calcular tiempo transcurrido
    elapsed_time = time.time() - start_time

    # Mostrar resultados en consola
    print("\n" + "=" * 60)
    print("RESULTADOS DE CONTEO DE PALABRAS")
    print("=" * 60)
    print(f"{'Palabra':<30} {'Frecuencia':<15}")
    print("-" * 60)

    # Mostrar las primeras 20 palabras más frecuentes
    display_limit = min(20, len(sorted_frequency))
    for i in range(display_limit):
        word, freq = sorted_frequency[i]
        print(f"{word:<30} {freq:<15}")

    if len(sorted_frequency) > display_limit:
        print(f"\n... y {len(sorted_frequency) - display_limit} "
              f"palabras más (ver archivo de resultados)")

    print("\n" + "=" * 60)
    print(f"Total de palabras: {len(words)}")
    print(f"Palabras distintas: {len(sorted_frequency)}")
    print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")

    # Escribir resultados en archivo
    output_file = "../results/WordCountResults.txt"
    write_results_to_file(output_file, sorted_frequency, len(words),
                          elapsed_time)
    print(f"\nResultados completos guardados en '{output_file}'")


if __name__ == "__main__":
    main()
