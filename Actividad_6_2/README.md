# Actividad 6.2 - Sistema de Reservaciones de Hotel

Este proyecto es un sistema completo para gestionar reservaciones de hotel, desarrollado en Python como parte de la Actividad 6.2 sobre pruebas unitarias y calidad de software.

## 👨‍💻 Autor
- **Matrícula**: A01021209
- **Actividad 6.2**
- **Fecha**: 22 de Febrero, 2026

## 📖 ¿Qué hace este programa?

El sistema permite administrar un hotel manejando tres componentes principales:
- **Hotel**: Controla la información de hoteles y cuántas habitaciones están disponibles
- **Cliente (Customer)**: Guarda los datos de los clientes que hacen reservaciones
- **Reservación (Reservation)**: Gestiona las reservas, fechas de entrada/salida y su estado

## ✨ Lo que incluye

-  Crear, modificar, consultar y eliminar hoteles, clientes y reservaciones
-  Los datos se guardan en archivos JSON para no perderlos
-  Valida que los datos sean correctos (fechas válidas, IDs únicos, etc.)
-  Maneja bien los errores cuando algo sale mal


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
Esto ejecuta las pruebas y te muestra cuáles pasaron.

### Ver la cobertura de código
```bash
python -m coverage run -m unittest discover -s tests
python -m coverage report -m
python -m coverage html
```
La cobertura te dice qué porcentaje del código fue ejecutado durante las pruebas.
## 🔍 Análisis de calidad del código

### Flake8 (verifica el estilo del código)
```bash
python -m flake8 source/ tests/ --max-line-length=79 --statistics
```

### Pylint (analiza la calidad del código)
```bash
python -m pylint source/hotel_reservation_system.py --max-line-length=79
```

##  Casos de prueba

### Casos negativos (23 pruebas) - Cuando las cosas salen mal
Estos casos verifican que el sistema maneje correctamente los errores:

**Pruebas con Hoteles:**
1. Intentar crear un hotel con un ID que ya existe
2. Crear un hotel con 0 habitaciones
3. Crear un hotel con número negativo de habitaciones
4. Borrar un hotel que no existe
5. Tratar de eliminar un hotel que tiene reservaciones activas
6. Modificar un hotel que no existe
7. Reducir las habitaciones de un hotel por debajo de las ya reservadas
8. Mostrar información de un hotel inexistente

**Pruebas con Clientes:**
9. Crear un cliente con un ID duplicado
10. Eliminar un cliente que no existe
11. Borrar un cliente que tiene reservaciones activas
12. Modificar datos de un cliente inexistente
13. Consultar un cliente que no está registrado

**Pruebas con Reservaciones:**
14. Hacer una reservación con un ID que ya se usó
15. Reservar para un cliente que no existe
16. Reservar en un hotel que no existe
17. Intentar reservar cuando no hay habitaciones disponibles
18. Usar un formato de fecha inválido (ej: "01-03-2026" en vez de "2026-03-01")
19. Poner fecha de salida antes que la de entrada
20. Hacer check-in y check-out el mismo día
21. Cancelar una reservación que no existe
22. Cancelar una reservación que ya fue cancelada
23. Intentar leer archivos JSON corruptos o con datos incorrectos

### Casos positivos (25 pruebas) - Cuando todo funciona bien
-  Crear, modificar, eliminar y consultar hoteles correctamente
-  Gestionar clientes sin problemas
-  Hacer y cancelar reservaciones
-  Guardar y cargar datos de archivos JSON
-  Actualizar automáticamente las habitaciones disponibles
-  Validar que los datos se guarden correctamente


## 📝 Commits en Git

Seguí la práctica de conventional commits:
- `feat:` - Cuando agregué código nuevo (ej: las clases principales)
- `test:` - Cuando agregué pruebas
- `docs:` - Para documentación y README
- `fix:` - Cuando arreglé errores (ej: los errores de flake8)


## 📌 Notas finales

Este proyecto me ayudó a entender mejor la importancia de:
- Probar el código exhaustivamente (incluyendo los casos donde falla)
- Seguir estándares de código para que otros lo puedan leer fácilmente  
- Usar herramientas de análisis estático como flake8 y pylint
- Medir la cobertura para asegurarme de que probé casi todo

---

