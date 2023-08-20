import streamlit as st
def main():
    st.title("Dashboard de Power BI en Streamlit")

    # Agrega el enlace público de tu dashboard de Power BI
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiYzkyMTUyMDYtMGNiNi00ZWQyLTg5MGYtNTMwY2NkNjkwYmQ2IiwidCI6IjUwNjIwMTJiLTI4NGEtNDJkNS1hOTk0LTk2ZTBiZmNlOTczNiIsImMiOjR9"
    st.markdown(f'<iframe src="{power_bi_url}" width="800" height="600" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()