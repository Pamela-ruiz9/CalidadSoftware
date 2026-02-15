"""
Programa para calcular el total de ventas.

Lee productos y ventas desde archivos JSON y calcula el total.
"""

import json
import sys


def load_json_file(filepath):
    """Cargar datos desde un archivo JSON."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado - {filepath}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Formato JSON inválido - {filepath}")
        sys.exit(1)


def build_price_catalog(products):
    """Crear un diccionario con los precios de los productos."""
    catalog = {}
    for product in products:
        catalog[product['title']] = product['price']
    return catalog


def calculate_total_sales(sales, price_catalog):
    """Calcular el total de ventas."""
    total = 0.0
    for sale in sales:
        product_name = sale['Product']
        quantity = sale['Quantity']
        if product_name in price_catalog:
            price = price_catalog[product_name]
            total += price * quantity
        else:
            print(f"Advertencia: Producto no encontrado - {product_name}")
    return total


def main():
    """Función principal."""
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py <ProductList.json> <Sales.json>")
        sys.exit(1)

    product_file = sys.argv[1]
    sales_file = sys.argv[2]

    # Cargar datos
    products = load_json_file(product_file)
    sales = load_json_file(sales_file)

    # Crear catálogo de precios
    price_catalog = build_price_catalog(products)

    # Calcular total
    total = calculate_total_sales(sales, price_catalog)

    # Mostrar resultado
    print(f"{total:.2f}")


if __name__ == "__main__":
    main()
