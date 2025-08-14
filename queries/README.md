# Scripts SQL para Crear Tablas

Este directorio contiene los scripts SQL para crear las tablas basadas en los archivos CSV del directorio `data/`.

## Estructura de las Tablas

### 1. Calendario (`01_create_calendario.sql`)
- **Propósito**: Tabla de dimensiones para fechas
- **Campos principales**: IdFecha, fecha, anio, mes, dia, trimestre, semana
- **Uso**: Análisis temporal de ventas

### 2. CanalDeVenta (`02_create_canal_venta.sql`)
- **Propósito**: Catálogo de canales de venta
- **Campos**: CODIGO, DESCRIPCION
- **Valores**: Telefónica, OnLine, Presencial

### 3. Clientes (`03_create_clientes.sql`)
- **Propósito**: Información de clientes
- **Campos principales**: ID, Nombre_y_Apellido, Provincia, Localidad, coordenadas (X,Y)
- **Nota**: Incluye campo `col10` del CSV original

### 4. Productos (`04_create_productos.sql`)
- **Propósito**: Catálogo de productos
- **Campos**: ID_PRODUCTO, Concepto, Tipo, Precio
- **Tipos**: INFORMATICA, IMPRESIÓN, AUDIO, GAMING, etc.

### 5. Sucursales (`05_create_sucursales.sql`)
- **Propósito**: Información de sucursales
- **Campos**: ID, Sucursal, Direccion, Localidad, Provincia, coordenadas

### 6. Venta (`06_create_venta.sql`)
- **Propósito**: Tabla de hechos de ventas
- **Campos**: IdVenta, Fechas, IDs de referencia, Precio, Cantidad
- **Foreign Keys**: Referencias a todas las tablas de dimensiones

## Orden de Ejecución

1. **00_create_all_tables.sql** - Script maestro que ejecuta todos los scripts en orden
2. **01_create_calendario.sql** - Sin dependencias
3. **02_create_canal_venta.sql** - Sin dependencias  
4. **03_create_clientes.sql** - Sin dependencias
5. **04_create_productos.sql** - Sin dependencias
6. **05_create_sucursales.sql** - Sin dependencias
7. **06_create_venta.sql** - Con foreign keys a todas las tablas anteriores

## Uso

```bash
# Ejecutar script maestro
psql -d tu_base_de_datos -f 00_create_all_tables.sql

# O ejecutar individualmente
psql -d tu_base_de_datos -f 01_create_calendario.sql
psql -d tu_base_de_datos -f 02_create_canal_venta.sql
# ... etc
```

## Características

- **IF NOT EXISTS**: Evita errores si las tablas ya existen
- **Índices**: Optimizados para consultas frecuentes
- **Foreign Keys**: Mantiene integridad referencial
- **Tipos de datos**: Apropiados para cada campo según el CSV
- **Constraints**: Validaciones básicas de datos
