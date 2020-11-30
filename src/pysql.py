'''
@Autor: Paulo https://github.com/alpdias
'''

# biblioteca de conexao entre o servidor do MySQL e o Python.
import pymysql 

def retornarConexao():
    
    """
    -> Funçao para realizar a conexão com um codigo Python e um banco de dado MySQL
    """

    conexao = pymysql.connect( 
        host = 'localhost', # servidor
        database = 'python', # banco de dados
        user = 'root', # usuario
        passwd = '', # senha
    )
    cursor = conexao.cursor() # Recebe a conexao MySQL
    
    return cursor


cursor = retornarConexao() # Recebe a conexao MySQL dentro da funçao
resultado = cursor.execute('SELECT * FROM pessoas') # recebe a solicitaçao dentro do MySQL para vizualizar a tabela

for resultado in cursor: # mostra o resultado da solicitação em linhas
    print(resultado)

