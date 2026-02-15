# Actividad 5.2 - Análisis Estático de Código

## Descripción
Programa en Python que calcula el total de ventas a partir de un catálogo de productos y un archivo de ventas.

## Estructura del Proyecto
```
Actividad5_2/
├── source/
│   └── computeSales.py       # Programa principal
├── tests/
│   ├── TC1/                  # Caso de prueba 1
│   ├── TC2/                  # Caso de prueba 2
│   └── TC3/                  # Caso de prueba 3
└── results/
    └── TestResults.txt       # Resultados de las pruebas
```

## Uso

```bash
python computeSales.py <ProductList.json> <Sales.json>
```

### Ejemplo
```bash
python computeSales.py tests/TC1/TC1.ProductList.json tests/TC1/TC1.Sales.json
```

## Verificación de Calidad

### Análisis Estático con flake8
```bash
flake8 source/computeSales.py
```

### Estándares Cumplidos
-  PEP-8 (Python Enhancement Proposal 8)
-  Sin errores de pycodestyle 
-  Sin errores de PyFlakes 
-  Complejidad ciclomática bajo control 

## Resultados de Pruebas

| Caso de Prueba | Esperado | Obtenido | Estado |
|----------------|----------|----------|--------|
| TC1            | 2481.86  | 2481.86  | OK     |
| TC2            | 166568.23| 166568.23| OK     |
| TC3            | 165235.37| 165235.37| OK     |


## Autor
Ingrid Pamela Ruiz Puga - A01021209

## Fecha
15 de febrero de 2026
