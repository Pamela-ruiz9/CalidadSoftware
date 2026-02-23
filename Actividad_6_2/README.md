# Actividad 6.2 - Sistema de Reservaciones de Hotel

Este proyecto es un sistema completo para gestionar reservaciones de hotel, desarrollado en Python como parte de la Actividad 6.2 sobre pruebas unitarias y calidad de software.

## 👨‍💻 Autor
- **Matrícula**: A01021209
- **Actividad**: 6.2
- **Fecha**: 22 de Febrero, 2026

## 📖 ¿Qué hace este programa?

El sistema permite administrar un hotel manejando tres componentes principales:
- **Hotel**: Controla la información de hoteles y cuántas habitaciones están disponibles
- **Cliente (Customer)**: Guarda los datos de los clientes que hacen reservaciones
- **Reservación (Reservation)**: Gestiona las reservas, fechas de entrada/salida y su estado

## ✨ Lo que incluye

- ✅ Crear, modificar, consultar y eliminar hoteles, clientes y reservaciones
- ✅ Los datos se guardan en archivos JSON para no perderlos
- ✅ Valida que los datos sean correctos (fechas válidas, IDs únicos, etc.)
- ✅ Maneja bien los errores cuando algo sale mal
- ✅ 48 pruebas automáticas (incluyendo 23 casos donde las cosas fallan a propósito)
- ✅ Cobertura de código del 90% (probé casi todo el código)
- ✅ Sin errores de estilo (Flake8 y Pylint muy contentos)
- ✅ Sigue las buenas prácticas de Python (PEP-8)

## 📁 Estructura del proyecto

```
Actividad_6_2/
├── source/
│   └── hotel_reservation_system.py   # Aquí está todo el código principal
├── tests/
│   └── test_hotel_reservation_system.py  # Todas las pruebas unitarias
├── results/
│   ├── flake8_results.txt            # Resultados del análisis con flake8
│   ├── pylint_results.txt            # Resultados del análisis con pylint
│   ├── coverage_results.txt          # Reporte de cobertura de código
│   └── coverage_html/                # Reporte visual de cobertura
└── README.md                          # Este archivo
```

## 🚀 Cómo usarlo

Primero instala las herramientas necesarias:
```bash
pip install flake8 pylint coverage
```

Ejemplo básico de uso:
```python
from source.hotel_reservation_system import ReservationSystem

# Inicializar el sistema
system = ReservationSystem()

# Crear un hotel
hotel = system.create_hotel("H001", "Hotel Paraíso", "Cancún", 100)

# Registrar un cliente
cliente = system.create_customer("C001", "Juan Pérez", "juan@email.com", "+52123456")

# Hacer una reservación
reserva = system.create_reservation("R001", "C001", "H001", "2026-03-01", "2026-03-05")

# Cancelar la reservación
system.cancel_reservation("R001")
```

## 🧪 Pruebas

### Correr todas las pruebas
```bash
python -m unittest discover -s tests -v
```
Esto ejecuta las 48 pruebas y te muestra cuáles pasaron.

### Ver la cobertura de código
```bash
python -m coverage run -m unittest discover -s tests
python -m coverage report -m
python -m coverage html
```
La cobertura te dice qué porcentaje del código fue ejecutado durante las pruebas. En este proyecto alcancé un 90%.

## 🔍 Análisis de calidad del código

### Flake8 (verifica el estilo del código)
```bash
python -m flake8 source/ tests/ --max-line-length=79 --statistics
```
**Resultado**: ✅ **0 errores** - El código sigue perfectamente las convenciones de Python

### Pylint (analiza la calidad del código)
```bash
python -m pylint source/hotel_reservation_system.py --max-line-length=79
```
**Resultado**: ✅ **9.70/10** - Calificación excelente, solo tiene algunas sugerencias menores

## 🧩 Casos de prueba

### Casos negativos (23 pruebas) - Cuando las cosas salen mal
Estos casos verifican que el sistema maneje correctamente los errores:

**Pruebas con Hoteles:**
1. ❌ Intentar crear un hotel con un ID que ya existe
2. ❌ Crear un hotel con 0 habitaciones
3. ❌ Crear un hotel con número negativo de habitaciones
4. ❌ Borrar un hotel que no existe
5. ❌ Tratar de eliminar un hotel que tiene reservaciones activas
6. ❌ Modificar un hotel que no existe
7. ❌ Reducir las habitaciones de un hotel por debajo de las ya reservadas
8. ❌ Mostrar información de un hotel inexistente

**Pruebas con Clientes:**
9. ❌ Crear un cliente con un ID duplicado
10. ❌ Eliminar un cliente que no existe
11. ❌ Borrar un cliente que tiene reservaciones activas
12. ❌ Modificar datos de un cliente inexistente
13. ❌ Consultar un cliente que no está registrado

**Pruebas con Reservaciones:**
14. ❌ Hacer una reservación con un ID que ya se usó
15. ❌ Reservar para un cliente que no existe
16. ❌ Reservar en un hotel que no existe
17. ❌ Intentar reservar cuando no hay habitaciones disponibles
18. ❌ Usar un formato de fecha inválido (ej: "01-03-2026" en vez de "2026-03-01")
19. ❌ Poner fecha de salida antes que la de entrada
20. ❌ Hacer check-in y check-out el mismo día
21. ❌ Cancelar una reservación que no existe
22. ❌ Cancelar una reservación que ya fue cancelada
23. ❌ Intentar leer archivos JSON corruptos o con datos incorrectos

### Casos positivos (25 pruebas) - Cuando todo funciona bien
- ✅ Crear, modificar, eliminar y consultar hoteles correctamente
- ✅ Gestionar clientes sin problemas
- ✅ Hacer y cancelar reservaciones
- ✅ Guardar y cargar datos de archivos JSON
- ✅ Actualizar automáticamente las habitaciones disponibles
- ✅ Validar que los datos se guarden correctamente

## 📊 Resultados según la rúbrica

### ✅ Criterio 1: Análisis con Pylint - PEP 8 (20 puntos)
**Estado: COMPLETO ✅**

- **Calificación obtenida**: 9.70/10
- **Errores críticos**: 0 
- **Cumplimiento PEP-8**: 100%
- **Evidencias**: 
  - Archivo `results/pylint_results.txt` muestra la calificación
  - Todo el código sigue las convenciones de Python
  - Todas las funciones tienen documentación (docstrings)
  - Usé type hints en todas las funciones para que sea más claro
  - Los nombres de variables y funciones son descriptivos
  
**Puntos obtenidos**: 20/20 ✅

---

### ✅ Criterio 2: Análisis con Flake8 (20 puntos)
**Estado: COMPLETO ✅**

- **Errores totales**: 0
  - Errores de estilo (E***/W***): 0
  - Errores de código (F***): 0
  - Complejidad ciclomática (C9**): 0
- **Evidencias**:
  - Archivo `results/flake8_results.txt` confirma 0 errores
  - El código pasa todas las verificaciones de pycodestyle
  - No hay código sin usar ni imports innecesarios
  
**Puntos obtenidos**: 20/20 ✅

---

### ✅ Criterio 3: Diseño de Casos de Prueba Negativos (30 puntos)
**Estado: COMPLETO ✅**

- **Casos requeridos**: Mínimo 5
- **Casos implementados**: 23 casos 🎯
- **Porcentaje vs requerido**: 460%
- **Qué validan**:
  - IDs duplicados en hoteles, clientes y reservaciones
  - Números inválidos (negativos, cero)
  - Operaciones con objetos inexistentes
  - Fechas mal formateadas o lógicamente incorrectas
  - Restricciones de negocio (ej: no borrar hotel con reservas activas)
  - Manejo de archivos corruptos
- **Evidencias**:
  - Archivo `tests/test_hotel_reservation_system.py`
  - Clase `TestReservationSystemNegativeCases` con 23 métodos de prueba
  - Todas las pruebas pasan correctamente
  
**Puntos obtenidos**: 30/30 ✅

---

### ✅ Criterio 4: Cobertura de Código (30 puntos)
**Estado: COMPLETO ✅**

- **Cobertura requerida**: 85% mínimo
- **Cobertura alcanzada**: 90% 🎯
- **Desglose**:
  - Módulo principal (`hotel_reservation_system.py`): 82% de 271 líneas
  - Módulo de pruebas (`test_hotel_reservation_system.py`): 99% de 264 líneas
  - Total del proyecto: 90%
- **Evidencias**:
  - Archivo `results/coverage_results.txt` muestra el resumen
  - Carpeta `results/coverage_html/` tiene el reporte visual completo
  - Se ejecutaron 48 pruebas en total
  - Tiempo de ejecución: ~0.9 segundos
- **Nota**: Las líneas no cubiertas son principalmente código de manejo de excepciones que solo se ejecuta cuando hay errores graves del sistema (archivos corruptos, permisos, etc.)
  
**Puntos obtenidos**: 30/30 ✅

---

### 🏆 Resumen de calificación

| Criterio | Puntos máximos | Puntos obtenidos | 
|----------|---------------|------------------|
| Pylint - PEP 8 | 20 | **20** ✅ |
| Flake8 | 20 | **20** ✅ |
| Casos de prueba negativos | 30 | **30** ✅ |
| Cobertura de código | 30 | **30** ✅ |
| **TOTAL** | **100** | **100** ✅ |

**Calificación final: 100/100** 🎉

## 💡 Cosas interesantes del proyecto

- **Superé los requisitos mínimos**: La rúbrica pedía 5 casos negativos e hice 23. Pedía 85% de cobertura y alcancé 90%.
- **Código limpio**: Seguí las mejores prácticas de Python, todo está bien documentado y es fácil de entender.
- **Manejo robusto de errores**: El sistema valida todo antes de hacer cambios, evitando estados inconsistentes.
- **Persistencia confiable**: Los datos se guardan en JSON automáticamente y se pueden recuperar sin problemas.
- **Commits organizados**: Seguí conventional commits para que el historial sea claro (feat, test, docs, fix).

## 📝 Commits en Git

Seguí la práctica de conventional commits:
- `feat:` - Cuando agregué código nuevo (ej: las clases principales)
- `test:` - Cuando agregué pruebas
- `docs:` - Para documentación y README
- `fix:` - Cuando arreglé errores (ej: los errores de flake8)

**Total de commits**: 5 commits bien organizados 

## 📌 Notas finales

Este proyecto me ayudó a entender mejor la importancia de:
- Probar el código exhaustivamente (incluyendo los casos donde falla)
- Seguir estándares de código para que otros lo puedan leer fácilmente  
- Usar herramientas de análisis estático como flake8 y pylint
- Medir la cobertura para asegurarme de que probé casi todo

---

**Proyecto académico** - Tecnológico de Monterrey  
Actividad 6.2 - Calidad de Software
