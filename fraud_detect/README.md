# 💳 Detección de fraudes con tarjetas de crédito

Este proyecto tiene como objetivo la detección de fraudes en transacciones con tarjetas de crédito utilizando técnicas avanzadas de análisis, 
visualización y aprendizaje automático de datos. Utilizamos un dataset descargado de [Kaggle](https://www.kaggle.com/) para analizar y modelar 
las transacciones, destacando las características más importantes que ayudan a identificar comportamientos fraudulentos. 🚀

## 🗂️ Tabla de contenidos

- 💡 Descripción
- 🛠️ Tecnologías empleadas
- 📝 Plan de trabajo
- 📊 Visualizaciones
- 🌳 Representación de árboles de decisión
- ⚙️ Modelo de Machine Learning
- 📋 Conclusiones

## 💡 Descripción

El proyecto busca identificar transacciones fraudulentas mediante técnicas de aprendizaje supervisado. A través de la exploración y análisis 
detallado del conjunto de datos, se identifican patrones relevantes y características clave que diferencian las transacciones legítimas de las 
fraudulentas. Finalmente, se construye un modelo predictivo capaz de clasificar con precisión las transacciones para detectar posibles fraudes. 🧐

## 🛠️ Tecnologías empleadas

- **Lenguaje**: 🐍 Python
- **Entorno de desarrollo**: Jupyter Notebooks 📒
- **Librerías**:
  - `numpy`
  - `pandas`
  - `seaborn`
  - `matplotlib`
  - `sklearn`
  - `plotly`
  - `cufflinks`

## 📝 Plan de trabajo

1. **Otención del dataset.**
2. **Importación de bibliotecas necesarias.**
3. **Organización del dataset.** 🗄️
4. **Limpieza de datos**: Eliminación de valores perdidos y duplicados.
5. **Análisis de datos**:
   - 🔢 Cálculo del porcentaje de transacciones fraudulentas.
   - 💰 Cálculo del importe medio de las transacciones fraudulentas.
6. **Visualización de datos**:
   - 📊 Relación de transacciones fraudulentas y no fraudulentas.
   - 📈 Distribución de los importes de las transacciones fraudulentas.
7. **Desarrollo y evaluación del modelo**:
   - 📂 Preparación de los datos: conjuntos de entrenamiento y prueba.
   - ⚙️ Creación y evaluación del modelo.
   - 📚 Generación de visualizaciones para análisis.
8. **Representación de árboles de decisión**: 
   - Generación de gráficos de árboles para visualizar cómo el modelo toma decisiones.

## 📊 Visualizaciones

Durante el proyecto se realizaron varias visualizaciones para explorar y entender mejor los datos y el modelo:

- **Gráfico de barras**: Comparación de transacciones fraudulentas y no fraudulentas.
- **Histograma**: Distribución de los importes de las transacciones fraudulentas.
- **Gráficos interactivos**: Gráficos de dispersión y KDE para analizar las relaciones entre variables como `Amount` y `Class` (fraudulenta/no fraudulenta).
- **Importancia de características**: Visualización de la relevancia de las variables clave.
- **Curvas ROC, AUC y PRC**: Evaluación del rendimiento del modelo. 📈

## 🌳 Representación de árboles de decisión

Para comprender cómo el modelo toma decisiones, se generaron gráficos de árboles de decisión simplificados utilizando el parámetro `max_depth`. 
Esto permite interpretar las decisiones del modelo de manera clara y comprensible. 🎯

Con estos gráficos, podemos visualizar las reglas que el modelo aplica para clasificar las transacciones, proporcionando una perspectiva transparente 
sobre su funcionamiento. 🧠

## ⚙️ Modelo de Machine Learning

El modelo principal utilizado en este proyecto ha sido el **Random Forest Classifier**. Este modelo fue seleccionado por su capacidad para manejar datos 
desbalanceados y por su robustez frente a características ruidosas.

El proceso de entrenamiento incluyó la separación de los datos en conjunto de entrenamiento y conjunto de prueba, la optimización de hiperparámetros 
y la evaluación del modelo en función de diversas métricas de rendimiento.

### Evaluación del Modelo

El modelo fue evaluado utilizando:

* Matriz de Confusión: Para medir la precisión de la clasificación en términos de verdaderos positivos, falsos positivos, etc.
* Curvas ROC y AUC: Para visualizar la capacidad del modelo para discriminar entre las clases.
* Curvas Precision-Recall (PRC) y AUC: Para evaluar el desempeño del modelo en situaciones con clases desbalanceadas.

## 📋 Conclusiones

Este proyecto presenta un enfoque práctico para la detección de fraudes con tarjetas de crédito utilizando Machine Learning. A través de la preparación 
de los datos, la construcción de un modelo predictivo y la visualización interactiva de los resultados, es posible detectar patrones fraudulentos con un 
alto grado de precisión.

Este proyecto sirve como una introducción a la aplicación de modelos de Machine Learning en la detección de fraudes, y demuestra cómo las visualizaciones 
interactivas pueden ayudar a interpretar y explicar los resultados de manera comprensible.

## 🫵 Ahora puedes probarlo tú

Descarga el [dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) y el notebook.

Instala las librerías necesarias:
```python
pip install numpy pandas seaborn matplotlib sklearn plotly cufflinks
```

- - - 

¡Gracias por leer este proyecto! 🚀 Si tienes alguna pregunta o sugerencia, no dudes en contactarme. 😄
