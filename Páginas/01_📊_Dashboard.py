import streamlit as st
def main():
    st.title("Dashboard de Power BI")

    st.write("""
             El panel de control muestra una parte del modelo de machine learning. Mediante el análisis de sentimientos llevado a cabo, calculamos un índice de satisfacción del cliente utilizando una fórmula DAX. Esto nos brinda la capacidad de evaluar el nivel de satisfacción de los usuarios de los hoteles en relación con los servicios ofrecidos, considerando los comentarios proporcionados por los mismos.
    """)
             
    # Agrega el enlace público de tu dashboard de Power BI
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiYzkyMTUyMDYtMGNiNi00ZWQyLTg5MGYtNTMwY2NkNjkwYmQ2IiwidCI6IjUwNjIwMTJiLTI4NGEtNDJkNS1hOTk0LTk2ZTBiZmNlOTczNiIsImMiOjR9"
    st.markdown(f'<iframe src="{power_bi_url}" width="800" height="600" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

    st.markdown('***') 
    
    st.write("""
            Además, analizamos otras métricas cruciales, como la calificación por estado o ciudad, que nos proporciona una visión de las evaluaciones dadas por los usuarios. Asimismo, examinamos la distribución del rating, permitiéndonos comprender el nivel de satisfacción de los usuarios en una escala que va del 1 al 5.
    """)

    st.markdown('***') 

    st.write("""
        Por otro lado, también es viable examinar tanto la calificación por hotel como el sentimiento asociado, ya sea positivo, negativo o neutro. Esto proporciona una perspectiva valiosa sobre cómo los usuarios están evaluando su cadena hotelera, y si es necesario implementar mejoras con el fin de elevar el rating o índice de satisfacción general.
    """)
             
if __name__ == "__main__":
    main()