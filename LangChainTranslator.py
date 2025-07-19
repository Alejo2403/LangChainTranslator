import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

apiIAKey = os.getenv("GROQ_API_KEY")
langChainAPIKey = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Traductor de frases GROQ"

st.title("Traductor GROK para frases")

texto  = st.text_input("Escribe una frase para traducir:")

idioma  = st.selectbox("Selecciona el idioma de traduccion:", ["Español", "Aleman", "Mandarin", "Ruso", "Ingles", "Portuges"])

if st.button("Traducir"):
    prompt = PromptTemplate.from_template("Eres un traductor profesional. Traduce el siguiente texto al idioma objetivo.\n\n""Idioma destino: {idioma}\nTexto original: {text}\n\nTraducción:")
    llm = ChatGroq(model_name = "llama3-8b-8192", temperature=0.7)
    chain = prompt | llm | StrOutputParser()

    resultado = chain.invoke({"text": texto, "idioma": idioma})
    st.success("Traduccion:")
    st.write(resultado)