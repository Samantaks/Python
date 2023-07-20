import mysql.connector
from faker import Faker

host = "localhost"
usuario = "root"
senha = "Z3R0l@ctose"
banco_de_dados = "bancoteste"

conexao = mysql.connector.connect(
    host = host,
    user = usuario,
    password = senha,
    database = banco_de_dados
)

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS professor(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(250),
    data_nascimento DATE,
    cidade_natal VARCHAR(250),
    estado VARCHAR(2),
    renda_percapta FLOAT,
    formacao VARCHAR(250)
)               
'''  
)

fake = Faker("pt-br")

dados_professor = []
for i in range (1,10001):
    nome = fake.name()
    data_nascimento = fake.date_of_birth()
    cidade_natal = fake.city()
    estado = fake.estado_sigla()
    renda_percapta = fake.pyfloat(left_digits = 4, right_digits = 2, positive = True)
    formacao = fake.text(max_nb_chars = 255)
    
    dados_professor.append((nome,data_nascimento,cidade_natal,estado,renda_percapta,formacao))
    

inserir_query = '''
INSERT INTO professor (
    nome, data_nascimento, cidade_natal, estado, renda_percapta, formacao               
    ) VALUES (%s,%s,%s,%s,%s,%s)
'''
cursor.executemany(inserir_query,dados_professor)

conexao.commit()
conexao.close()