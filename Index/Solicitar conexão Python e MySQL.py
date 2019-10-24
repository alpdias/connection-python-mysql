'''
@Autor: Paulo Alcântara https://github.com/alpdias
'''
import FuncaoDeConexao # Biblioteca com a função de conexão entre Python e o MySQL.

cursor = FuncaoDeConexao.RetornarConexaoMySQL() # Variável 'cursor' recebe a conexão MySQL.
resultado = cursor.execute('SELECT * FROM pessoas') # Variável 'resultado' recebe a solicitação dentro do MySQL.
for resultado in cursor: # Mostra o resultado da solicitação.
    print(resultado)
