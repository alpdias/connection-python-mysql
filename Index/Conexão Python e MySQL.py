'''
@Autor: Paulo Alcântara https://github.com/alpdias
'''
import pymysql # Biblioteca de conexão Python e MySQL.

# Script para fazer a conexão.
conexao = pymysql.connect( 
    host = 'localhost', # Servidor.
    database = 'python', # Banco de dados.
    user = 'root', # Usuário.
    passwd = '', # Senha.
)
cursor = conexao.cursor() # Recebe a conexão MySQL.
cursor.execute('SELECT * FROM pessoas') # Envia comando ao MySQL.

for resultado in cursor: # Mostra o resultado solicitado.
    print(resultado)
