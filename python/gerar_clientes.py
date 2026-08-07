import mysql.connector
import random

nomes = ["Ana", "João", "Maria", "Pedro", "Lucas", "Julia"]
cidades = ["Juazeiro", "Recife", "Salvador", "Fortaleza"]
generos = ["Feminino", "Masculino"]

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sales"
)

cursor = conexao.cursor()

for i in range(10):
    nome = random.choice(nomes)
    genero = random.choice(generos)
    cidade = random.choice(cidades)

    sql = """
    INSERT INTO customers (name, gender, city)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, genero, cidade))

conexao.commit()

print("10 clientes inseridos!")

cursor.close()
conexao.close()


