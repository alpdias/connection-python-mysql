'''
@Autor: Paulo Alcântara https://github.com/alpdias
'''
import Funcao # Biblioteca com a função de conexão entre Python e o MySQL.

cursor = Funcao.RetornarConexaoMySQL() # Recebe a conexão MySQL.
resultado = cursor.execute('SELECT * FROM pessoas') # Recebe a solicitação dentro do MySQL.
for resultado in cursor: # Mostra o resultado da solicitação.
    print(resultado)
