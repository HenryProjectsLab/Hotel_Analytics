import streamlit as st

def main():
    st.title("Análisis de Sentimientos")
    
    st.text_area("Ingresa tu comentario:", height=150)
    
    st.button("Analizar Sentimiento")

if __name__ == "__main__":
    main()