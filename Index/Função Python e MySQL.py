'''
@Autor: Paulo Alcântara https://github.com/alpdias
'''
# Função para realizar conexão com o banco de dados MySQL e o código Python.
def RetornarConexaoMySQL():
    import pymysql # Biblioteca de conexão entre o servidor do MySQL e o Python.
    conexao = pymysql.connect( # Variável que recebe as configurações de conexão.
        host = 'localhost', # Servidor.
        database = 'python', # Banco de dados.
        user = 'root', # Usuário.
        passwd = '', # Senha.
    )
    cursor = conexao.cursor() # Recebe a conexão MySQL.
    return cursor


cursor = Função.RetornarConexaoMySQL() # Recebe a conexão MySQL.
resultado = cursor.execute('SELECT * FROM pessoas') # Recebe a solicitação dentro do MySQL.
for resultado in cursor: # Mostra o resultado da solicitação.
    print(resultado)
