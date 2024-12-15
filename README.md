# Hadoop-Mateo | Proyecto MapReduce

## Descripción
Este repositorio contiene la implementación de varios ejercicios basados en MapReduce. Cada ejercicio está organizado en carpetas individuales y utiliza scripts `mapper` y `reducer` para procesar los datos.

## Estructura del Proyecto

```plaintext
mapreduce/
│
├── Exercicio1.1/                  # Ejercicio 1.1: Descartar líneas con formato incorrecto
│   ├── DESCARTEFORMATO/           
│   │   ├── comando.txt
│   │   ├── mapper.py
│
├── Exercicio1.2/                  # Ejercicio 1.2: Total de ventas por categoría
│   ├── COMPRASXCATEGORIA/         
│   │   ├── comando.txt
│   │   ├── mapper2.py
│   │   ├── reducer2.py
│   │   └── mini_purchases.txt
│
├── Exercicio1.3/                  # Ejercicio 1.3: Venta más alta por tipo de pago
│   ├── VENTAMASALTA/              
│   │   ├── comando.txt
│   │   ├── mapper_max.py
│   │   └── reducer_max.py
│
├── Exercicio1.4/                  # Ejercicio 1.4: Máximo absoluto de las ventas
│   ├── MAXABSOLUTO/               
│   │   ├── comando.txt
│   │   ├── mapper_max.py
│   │   └── reducer_max.py
│
├── Exercicio1.5/                  # Ejercicio 1.5: Total de ventas
│   ├── TOTALVENTAS/               
│   │   ├── comando.txt
│   │   ├── mapper_max.py
│   │   ├── reducer_max.py
│   │   └── mini_purchases2.txt
│
├── .gitignore                     # Archivo para excluir archivos no deseados
├── LICENSE                        # Licencia del proyecto
└── README.md                      # Documentación del proyecto

---

## **Requisitos Previos**

1. **Python** instalado.
2. **Hadoop** configurado (para ejecución en clúster).
3. Permisos para ejecutar scripts:
   ```bash
   chmod +x mapper.py reducer.py
   ```

---

## **Instrucciones de Ejecución**

### **Ejecución Local**

Para probar el código localmente con un archivo pequeño:

1. **Crear un archivo de prueba:**
   ```bash
   head -n100 purchases.txt > mini_purchases.txt
   ```

2. **Ejecutar el mapper y el reducer localmente:**
   ```bash
   cat mini_purchases.txt | ./mapper.py | sort | ./reducer.py
   ```

3. **Verificar la salida:**
   La salida se imprimirá en la consola.

---

### **Ejecución en Hadoop**

1. **Subir los archivos de datos a HDFS:**
   ```bash
   hdfs dfs -put PURCHASE/purchases.txt
   ```

2. **Lanzar el trabajo MapReduce:**
   ```bash
   mapred streaming -files mapper.py,reducer.py \
       -input purchases.txt \
       -output nombre_salida \
       -mapper mapper.py \
       -reducer reducer.py
   ```

3. **Verificar los resultados en HDFS:**
   ```bash
   hdfs dfs -get nombre_salida
   cd nombre_salida
   cat *
   ```

---

## **Descripción de los Ejercicios**

### **Exercicio 1.1: Filtrado de líneas con formato incorrecto**
- **Objetivo:** Mejorar el mapper para descartar líneas con un formato no válido.
- **Solución:** El mapper verifica si la línea contiene el número correcto de campos.

### **Exercicio 1.2: Total de ventas por categoría**
- **Objetivo:** Calcular el total de ventas agrupadas por categoría.
- **Mapper:** Emite la categoría y el valor de la venta.
- **Reducer:** Suma las ventas por categoría.

### **Exercicio 1.3: Venta más alta por tipo de pago**
- **Objetivo:** Encontrar la venta máxima registrada para cada tipo de pago.
- **Mapper:** Emite el tipo de pago y el valor de la venta.
- **Reducer:** Calcula el valor máximo para cada tipo de pago.

### **Exercicio 1.4: Máximo absoluto de las ventas**
- **Objetivo:** Encontrar la venta máxima entre todas las ventas registradas.
- **Mapper:** Emite una etiqueta común y el valor de la venta.
- **Reducer:** Encuentra el valor máximo absoluto.

### **Exercicio 1.5: Total de todas las ventas**
- **Objetivo:** Calcular el total global de ventas.
- **Mapper:** Emite una etiqueta común y el valor de la venta.
- **Reducer:** Suma todas las ventas.

---

## **Créditos**

Desarrollado por Mateo para comprender el funcionamiento del trabajo distribuido usando MapReduce en Hadoop.

