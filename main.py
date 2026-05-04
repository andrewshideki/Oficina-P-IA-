# Aula 5 - Streamlit
# - biblioteca para Front-End
# aulas passadas: dicionário e caixeiro viajante

import streamlit as st

st.title("Aula de Streamlit", anchor=False, help=None, text_alignment="center") # -> anchor = link, help = texto em cima

st.header("Aula 5 - Professor Diego", anchor=False, help=None, divider="orange")

st.write("Olá, Mundo!") # -> escreve em um site criado local

code = '''print("Olá, Mundo!")''' # ou "print('Hello, World!')" #mostra um código

st.code(code, language="python")

st.button(label="Botãozinho", key="botaozinho" ,help="Clique nesse botão", type="primary") # label=texto, key=identidade
st.button(label="Botãozinho 2", key="botaozinho2" ,help="Clique nesse botão também", type="secondary")
st.button(label="Botãozinho 3", key="botaozinho3" ,help="E nesse também", type="tertiary")

contador = 0 # está resetando toda vez que o site atualiza
if st.button(label="Botão", help="Esse botão funciona!"):
    st.write("Parabéns! Você clicou no botão!")
    contador += 1
    st.badge(label=f"{contador}")

colA, colB, colC = st.columns(3)

with colA:
    st.write("Esta é a coluna A")

with colB:
    st.write("Esta é a coluna B")

with colC:
    st.write("Está é a coluna C")


# $pip download streamlit
# $pip 