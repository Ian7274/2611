import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="loja"

    )

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
          CREATE TABLE IF NOT EXISTS produto(
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                preco DECIMAL(10,2)
        )
""")
    conexao.commit() 
    cursor.close()
    conexao.close()

def inserir_produto(nome, preco):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produto(nome, preco) VALUES (%s, %s)", (nome, preco))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return dados