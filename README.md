# buscador-tfidf
Sistema de recuperación de información en Python que utiliza preprocesamiento de lenguaje natural, TF-IDF y similitud del coseno para realizar búsquedas sobre un corpus de documentos médicos.

Este proyecto implementa un sistema de recuperación de información desarrollado en Python. El sistema procesa un corpus de documentos médicos y permite realizar consultas de texto libre para recuperar los documentos más relevantes.

## Características

- Tokenización de texto.
- Conversión a minúsculas.
- Eliminación de signos de puntuación.
- Conversión de números a texto.
- Eliminación de stopwords.
- Lematización.
- Construcción de bolsas de palabras.
- Cálculo de pesos TF-IDF.
- Ranking de documentos mediante similitud del coseno.

## Tecnologías utilizadas

- Python
- NLTK
- Scikit-learn
- NumPy
- Pandas
- Matplotlib

## Funcionamiento

El usuario introduce una consulta en lenguaje natural. La consulta se normaliza utilizando el mismo proceso aplicado al corpus y posteriormente se calcula la similitud del coseno entre la consulta y todos los documentos indexados. Finalmente, el sistema muestra un ranking de los documentos más relevantes.

# https://youtu.be/TNjPMilIZ0o
