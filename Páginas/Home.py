import streamlit as st
from PIL import Image

def main():

    st.title("Data Wise Solutions")

    st.markdown('***') 

    st.header("Análisis de reseñas de hoteles usando Machine Learning")

    st.write("""
    Nuestra empresa de Consultoría, Data Wise Solutions DWS, se especializa en la organización, clasificación y procesamiento de los datos proporcionados por nuestros clientes, generando informes completos y detallados. En esta ocasión, nuestro compromiso es brindar un enfoque analítico integral para extraer información valiosa de los datos, con el objetivo de ofrecer a nuestros clientes una visión clara y precisa del estado actual de su negocio.
    """)

    st.markdown('***') 

    st.subheader("Contexto")

    st.write("""
    En esta ocasión, llevamos a cabo un análisis exhaustivo de los comentarios y reseñas proporcionados por los usuarios de diversos hoteles. El objetivo principal es identificar las áreas en las que los clientes han expresado su insatisfacción o preocupación en relación con los servicios ofrecidos. Para lograrlo, empleamos técnicas de análisis de sentimientos mediante el uso de la biblioteca VADER (Valence Aware Dictionary and sEntiment Reasoner) y la librería FastText. La meta es generar tópicos o temáticas clave a partir de esta información, con el propósito de ofrecer recomendaciones valiosas a nuestro cliente.
    """)

    st.markdown('***') 

    st.subheader("Objetivos")

    st.write("""
    - Conocer los principales aspectos de la industria hotelera en Estados Unidos, además de analizar las reseñas de los usuarios usando un modelo de ML.
    - Por medio del diagrama de arquitectura explicar el flujo del dato.
    - Entender cómo se cargan los datos a Google Cloud desde su origen.
    - Hacer una demostración de carga incremental en el Datawarehouse.
    - Presentar un dashboard en PowerBI con KPI’s del caso de estudio.
    - Dar a conocer algunos hallazgos relevantes adicionales.
    """)

    st.markdown('***') 

    st.subheader("KPI's")

    st.write("""
    Los indicadores de desempeño que se emplearon para analizar la información son los siguientes:

    - Índice de Satisfacción del Cliente: Evalúa la satisfacción general de los usuarios en relación con los productos/servicios mediante el análisis de los sentimientos expresados en las reseñas proporcionadas.
    - Promedio de Rating por Ciudad o Estado: Calcula el promedio de los valores de 'rating' para analizar cómo califican los usuarios los hoteles en diferentes ciudades o estados.
    - Distribución de Ratings: Analiza la distribución de los valores de 'rating' para entender la proporción de reseñas positivas, neutrales y negativas.
    - Promedio de Rating por Hotel: Calcula el promedio de los valores de 'rating para analizar cómo califican los usuarios una cadena hotelera o un hotel en particular.
    - Promedio de Sentimiento por Hotel: Calcula el promedio del sentimiento en las categorías positiva (1), negativa (0) y neutra (-1), teniendo en cuenta la percepción de los usuarios.
    - % Crecimiento de la ocupación 2019 vs. 2023: Indica la proporción en la que ha crecido la ocupación hotelera, en el periodo de tiempo indicado.
    """)

    st.markdown('***') 

    st.subheader("Stack Tecnológico")

    st.write("""
    Una lista de tecnologías utilizadas en el proyecto:

    - Python
    - SQL
    - Google Cloud Platform
    - Power Bi
    - Git
    - Jira
    """)

    st.markdown('***') 

    st.subheader("Colaboradores")

    st.write("""
    En este proyecto contribuyeron las siguientes personas:

    - Andrea Huertas
    - Franco Ccapa
    - Joaquin Olea
    - Jeison Suárez
    - Tomas Alvarenga
    """)

if __name__ == "__main__":
    main()
