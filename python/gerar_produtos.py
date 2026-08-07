import mysql.connector
import random

# Produto -> Categoria
produtos = {
    "Livro": "Papelaria",
    "Caneta": "Papelaria",
    "Arroz": "Graos",
    "Feijao": "Graos",
    "Suco": "Bebidas",
    "Refrigerante": "Bebidas"
}

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sales"
)

cursor = conexao.cursor()

sql = """
INSERT INTO products (product_name, category, price)
VALUES (%s, %s, %s)
"""

for i in range(10):

    # Escolhe um produto aleatório
    product_name = random.choice(list(produtos.keys()))

    # Busca a categoria correta desse produto
    category = produtos[product_name]

    # Gera um preço aleatório entre 1 e 50
    price = round(random.uniform(1, 50), 2)

    cursor.execute(sql, (product_name, category, price))

conexao.commit()

print("10 produtos inseridos!")

cursor.close()
conexao.close()

