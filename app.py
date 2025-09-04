import streamlit as st

# Título da aplicação
st.title("Remover Espaços e Caracteres Especiais")

# Caixa de texto para entrada do número da NF
nf_input = st.text_input("Digite um número para remover os espaços e caracteres especiais: ")

# Se o usuário digitar algo, remover tudo que não for número
if nf_input:
    nf_limpa = "".join(c for c in nf_input if c.isdigit())
    st.success(f"Número corrigido: {nf_limpa}")
