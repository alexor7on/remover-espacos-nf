import streamlit as st

# Título da aplicação
st.title("Remover espaços e caracteres")

# Caixa de texto para entrada do número da NF
nf_input = st.text_input("Digite o número da NF: ")

# Se o usuário digitar algo, remover tudo que não for número
if nf_input:
    nf_limpa = "".join(c for c in nf_input if c.isdigit())
    st.success(f"NF apenas com números: {nf_limpa}")
