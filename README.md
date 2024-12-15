# Hadoop-Mateo


# Proyecto MapReduce

Este repositorio contiene implementaciones de algoritmos MapReduce para procesar archivos de datos distribuidos. Cada ejercicio implementa un objetivo específico utilizando scripts de **mapper** y **reducer**.

---

## **Estructura del Proyecto**

``` 
mapreduce/
|
├── exercicio1_1/        # Descarta líneas con formato incorrecto
│   ├── mapper.py        # Código del mapper
│   ├── reducer.py       # Código del reducer
│   └── mini_purchases.txt # Archivo de prueba
│
├── exercicio1_2/        # Total de ventas por categoría
│   ├── mapper.py
│   ├── reducer.py
│   └── mini_purchases.txt
│
├── exercicio1_3/        # Venta más alta por tipo de pago
│   ├── mapper.py
│   ├── reducer.py
│   └── mini_purchases.txt
│
├── exercicio1_4/        # Máximo absoluto de las ventas
│   ├── mapper.py
│   ├── reducer.py
│   └── mini_purchases.txt
│
├── exercicio1_5/        # Total de todas las ventas
│   ├── mapper.py
│   ├── reducer.py
│   └── mini_purchases.txt
│
└── README.md            # Documentación del proyecto
```

---

## **Requisitos Previos**

1. **Python 3** instalado.
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
   hdfs dfs -put purchases.txt
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
   hdfs dfs -cat nombre_salida/part-00000
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

## **Enlace al Repositorio**

Este proyecto está disponible en: **[Tu enlace aquí]**

---

## **Créditos**

Desarrollado por [Tu Nombre] para comprender el funcionamiento del trabajo distribuido usando MapReduce en Hadoop.

