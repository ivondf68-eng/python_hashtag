#streamlit - frontend e backend
#openai - IA
import time

#Passo a passo:
#Passo 1: Importar streamlit e openai
import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="(neste local se coloca a API Key própria gerada no site da OpenAi)")

#Passo 1: Título (Markdown)
st.write("## ChatBot com IA")

#Passo 2: Input do chat
    #Verficando primeiro se já não tem uma lista de mensagens existente no chat do usuário, usando a memória do streamlit (session_state)
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

#Passo 3: Mostrar mensagem enviada:

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

#Mostra a mensagem do usuário e adiciona na lista de mensagens
if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    #Mostrar a resposta da IA no chat e adicionar na lista
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-5"
    )
    texto_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_ia)
    mensagem_ia = {"role": "assistant", "content": texto_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)