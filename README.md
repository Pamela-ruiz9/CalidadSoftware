## Autor

Matrícula: A01021209
Nombre: Ingrid Pamela Ruiz P

## Fecha

Febrero 2026

Actividad 4.2 - Ejercicios de Programación en Python

## Descripción

Tres programas en Python para la Actividad 4.2:

### 1. computeStatistics.py
Calcula estadísticas descriptivas (media, mediana, moda, varianza, desviación estándar) de números contenidos en un archivo.

**Uso:**
```bash
python computeStatistics.py fileWithData.txt
```

**Características:**
- Lee números desde un archivo
- Maneja errores de datos inválidos
- Calcula todas las estadísticas usando algoritmos básicos (sin librerías)
- Guarda resultados en `StatisticsResults.txt`
- Muestra tiempo de ejecución

### 2. convertNumbers.py
Convierte números decimales a binario y hexadecimal.

**Uso:**
```bash
python convertNumbers.py fileWithData.txt
```

**Características:**
- Lee números desde un archivo
- Convierte a binario y hexadecimal usando algoritmos básicos
- Maneja errores de datos inválidos
- Guarda resultados en `ConvertionResults.txt`
- Muestra tiempo de ejecución

### 3. wordCount.py
Cuenta la frecuencia de palabras en un archivo de texto.

**Uso:**
```bash
python wordCount.py fileWithData.txt
```

**Características:**
- Lee palabras desde un archivo
- Cuenta frecuencia de cada palabra
- Ordena por frecuencia (de mayor a menor)
- Maneja datos inválidos
- Guarda resultados en `WordCountResults.txt`
- Muestra tiempo de ejecución

## Archivos de Prueba

- `testNumbers.txt`: Archivo de prueba con números para computeStatistics.py y convertNumbers.py
- `testWords.txt`: Archivo de prueba con texto para wordCount.py

## Verificación con PyLint

Todos los programas han sido verificados con pylint y obtienen calificaciones superiores a 9.90/10.

```bash
pylint computeStatistics.py  # 9.92/10
pylint convertNumbers.py     # 9.90/10
pylint wordCount.py          # 9.90/10
```

## Requisitos

- Python 3.x
- pylint (para verificación de código)

## Instalación de pylint

```bash
pip install pylint
```


