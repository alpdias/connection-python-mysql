'''
@Autor: Paulo https://github.com/alpdias
'''
# Função para realizar a conexão com um código Python e um banco de dado MySQL.
def retornarConexao():
    import pymysql # Biblioteca de conexão entre o servidor do MySQL e o Python.
    conexao = pymysql.connect( 
        host = 'localhost', # Servidor.
        database = 'python', # Banco de dados.
        user = 'root', # Usuário.
        passwd = '', # Senha.
    )
    cursor = conexao.cursor() # Recebe a conexão MySQL.
    return cursor

print('')
cursor = retornarConexao() # Recebe a conexão MySQL dentro da função.
resultado = cursor.execute('SELECT * FROM pessoas') # Recebe a solicitação dentro do MySQL para vizualizar a tabela.
print('')
for resultado in cursor: # Mostra o resultado da solicitação em linhas.
    print(resultado)
print('')
