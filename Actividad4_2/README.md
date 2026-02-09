# Actividad 4.2 - Ejercicios de Programación en Python

**Matrícula:** A01021209  
**Fecha:** Febrero 2026

## Estructura del Proyecto

```
4.2/
├── P1/ (Estadísticas Descriptivas)
│   ├── source/
│   │   └── computeStatistics.py
│   ├── tests/
│   │   ├── TC1.txt
│   │   ├── TC2.txt
│   │   ├── TC3.txt
│   │   ├── TC4.txt
│   │   ├── TC5.txt
│   │   ├── TC6.txt
│   │   └── TC7.txt
│   └── results/
│       └── StatisticsResults.txt
│
├── P2/ (Conversión de Números)
│   ├── source/
│   │   └── convertNumbers.py
│   ├── tests/
│   │   ├── TC1.txt
│   │   ├── TC2.txt
│   │   ├── TC3.txt
│   │   └── TC4.txt
│   └── results/
│       └── ConvertionResults.txt
│
└── P3/ (Contador de Palabras)
    ├── source/
    │   └── wordCount.py
    ├── tests/
    │   ├── TC1.txt
    │   ├── TC2.txt
    │   ├── TC3.txt
    │   ├── TC4.txt
    │   └── TC5.txt
    └── results/
        └── WordCountResults.txt
```

## Programas Implementados

### P1: computeStatistics.py

Calcula estadísticas descriptivas **poblacionales** de números contenidos en un archivo.

**Estadísticas calculadas:**
- Media
- Mediana
- Moda
- Varianza Poblacional
- Desviación Estándar Poblacional

**Uso:**
```bash
cd 4.2/P1/source
python computeStatistics.py ../tests/TC1.txt
```

**Características:**
- Algoritmos implementados desde cero (sin usar librerías como numpy o statistics)
- Validación de datos de entrada
- Los resultados se guardan en `../results/StatisticsResults.txt`
- Incluye medición de tiempo de ejecución
- Código verificado con PyLint (9.92/10)

### P2: convertNumbers.py

Convierte números decimales a binario y hexadecimal.

**Uso:**
```bash
cd 4.2/P2/source
python convertNumbers.py ../tests/TC1.txt
```

**Características:**
- Conversión implementada con algoritmos básicos (sin usar bin() o hex())
- Validación de entrada
- Resultados en `../results/ConvertionResults.txt`
- Medición de tiempo de ejecución
- PyLint: 9.90/10

### P3: wordCount.py

Cuenta la frecuencia de palabras en un archivo de texto.

**Uso:**
```bash
cd 4.2/P3/source
python wordCount.py ../tests/TC1.txt
```

**Características:**
- Conteo de frecuencia de palabras (case-insensitive)
- Ordenamiento por frecuencia usando bubble sort
- Resultados en `../results/WordCountResults.txt`
- Tiempo de ejecución incluido
- PyLint: 9.90/10

## Requisitos

- Python 3.x
- pylint (para verificación de código)

## Instalación

1. Instalar pylint:
```bash
pip install pylint
```

2. Clonar el repositorio:
```bash
git clone <URL_REPOSITORIO>
cd <NOMBRE_REPOSITORIO>
```

## Ejecución de Pruebas

### P1 - Estadísticas Descriptivas

```bash
cd 4.2/P1/source
python computeStatistics.py ../tests/TC1.txt
python computeStatistics.py ../tests/TC2.txt
python computeStatistics.py ../tests/TC3.txt
# ... y así con TC4, TC5, TC6, TC7
```

### P2 - Conversión de Números

```bash
cd 4.2/P2/source
python convertNumbers.py ../tests/TC1.txt
python convertNumbers.py ../tests/TC2.txt
python convertNumbers.py ../tests/TC3.txt
python convertNumbers.py ../tests/TC4.txt
```

### P3 - Contador de Palabras

```bash
cd 4.2/P3/source
python wordCount.py ../tests/TC1.txt
python wordCount.py ../tests/TC2.txt
python wordCount.py ../tests/TC3.txt
python wordCount.py ../tests/TC4.txt
python wordCount.py ../tests/TC5.txt
```

## Verificación con PyLint

```bash
cd 4.2/P1/source
pylint computeStatistics.py

cd ../P2/source
pylint convertNumbers.py

cd ../P3/source
pylint wordCount.py
```

## Resultados

Los resultados de cada ejecución se guardan en las carpetas `results` de cada programa:
- `4.2/P1/results/StatisticsResults.txt`
- `4.2/P2/results/ConvertionResults.txt`
- `4.2/P3/results/WordCountResults.txt`

## Notas Importantes

1. **Varianza y Desviación Estándar:** Se utilizan las fórmulas **poblacionales** (dividir entre N), no las muestrales (dividir entre N-1), según las indicaciones adicionales del profesor.

2. **Nombres de archivos:** Aunque algunos nombres de archivos no siguen estrictamente snake_case (como `computeStatistics.py`), esto fue especificado en los requisitos originales del proyecto. Las indicaciones adicionales aclaran que esto es aceptable.

3. **Algoritmos básicos:** Todos los cálculos se implementan sin usar librerías especializadas (sin numpy, sin statistics, sin funciones built-in como bin() o hex()).

## Puntos Clave

- Los tres programas están en Python siguiendo PEP-8
- Todos los cálculos/conversiones usan algoritmos básicos
- Validación de entrada en todos los casos
- Argumentos por línea de comandos
- Resultados guardados en archivos de texto
- Tiempos de ejecución registrados
- Códigos verificados con PyLint (calificaciones arriba de 9.90)

## Autor

**Matrícula:** A01021209  
**Curso:** Pruebas y Calidad de Software  
**Actividad:** 4.2 - Ejercicios de Programación
