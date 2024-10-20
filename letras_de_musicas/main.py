import requests
import streamlit as st


def buscador(banda, musica):
    api = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(api)
    if response.status_code == 200:
        st.success("ucesso encotramos a letra... :)")
        st.write(response.json()['lyrics'])
    else:
        st.error("Infelizmente não localizamos a Letra... :( ")
        st.write("Pesquisa Inválida, tente novamente...")


st.image("logo.png")
st.title('Letras e Letras')
banda = st.text_input("Nome da banda: ", key='banda')
musica = st.text_input('Nome da musica: ', key='musica')
pesquisar = st.button("Pesquisar")

if pesquisar  :
    buscador(banda, musica)
