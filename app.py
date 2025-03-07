import streamlit as st

# Título da aplicação
st.title("Remover Espaços da Nota Fiscal")

# Caixa de texto para entrada do número da NF
nf_input = st.text_input("Digite o número da NF com espaços: ")

# Se o usuário digitar algo, remover espaços e mostrar o resultado
if nf_input:
    nf_limpa = "".join(c for c in nf_input if not c.isspace())
    st.success(f"NF sem espaços: {nf_limpa}")