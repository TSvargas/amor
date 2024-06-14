import streamlit as st 
from unicodedata import normalize
import time
import csv

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
namecheck = st.text_input("Nome Completo", placeholder="insira o nome do amor da minha vida")
namecheck = namecheck.lower()
namecheck = namecheck.title()
if len(namecheck) != 0:
    st.write('Interessante, continue...') 

regist = st.button('Checar', type= "primary")
if regist:
    if namecheck == "Ingrid Da Silva Rangel E Souza":
        st.write('UOOOU, você é o amor da minha vida!!')
        time.sleep(2)
        st.switch_page("https://linhatempo.streamlit.app/")   
    if namecheck == 'Ingrid':
        st.write('Hmmmmm, diga mais')
    elif namecheck != 'Ingrid' and namecheck != 'Ingrid Da Silva Rangel E Souza':
        st.write('Parece que você não é o amor da minha vida...')




