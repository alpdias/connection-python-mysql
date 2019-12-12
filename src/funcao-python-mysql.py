'''
@Autor: Paulo https://github.com/alpdias
'''
# Função para realizar a conexão em um código Python e um banco de dado MySQL.
def retornarConexao():
    import pymysql # Biblioteca de conexão entre o servidor do MySQL e o Python.
    conexao = pymysql.connect( # Variável que recebe as configurações de conexão.
        host = 'localhost', # Servidor.
        database = 'python', # Banco de dados.
        user = 'root', # Usuário.
        passwd = '', # Senha.
    )
    cursor = conexao.cursor() # Recebe a conexão MySQL.
    return cursor


cursor = Função.retornarConexao() # Recebe a conexão MySQL.
resultado = cursor.execute('SELECT * FROM pessoas') # Recebe a solicitação dentro do MySQL.
for resultado in cursor: # Mostra o resultado da solicitação.
    print(resultado)
