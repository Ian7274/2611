import streamlit as st
import db 

db.criar_tabela()
st.title("Loja de Vendas Python + Mysql + Streamlit")

menu = st.sidebar.selectbox("Menu", ["Cadastrar Produto", "Listar Produto"])
if menu == "Cadastrar Produto":
    st.subheader("Cadastrar Produto")
    nome = st.text_input("Nome do Produto")
    preco = st.number_input("Preço (R$)", min_value=0.0, format="%.2f")

    if st.button("Salvar Produto"):
        if nome and preco > 0:
            db.inserir_produto(nome, preco)
            st.success(f"Produto '{nome}' cadastro com sucesso")
        else:
            st.error("Preencha os campos corretamente!")

elif menu == "Listar Produtos":
    st.subheader("Lista de Produto")
    produtos = db.listar_produtos()
    if produtos: 
        for p in produtos:
            st.write(f"ID: {p[0]} | {p[1]} | {p[2]}")
        else:
            st.info("Nenhum produto cadastrado ainda!")
