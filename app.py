import sqlite3

nome = 'Teteu'
idade = 17
id = 111

banco = sqlite3.connect('primeiro_banco.db') # Criando o banco de dados

cursor = banco.cursor() # Colocando cursor no banco (excluir tabela, inserir registros, etc)

#cursor.execute('CREATE TABLE IF NOT EXISTS alunos (nome text, idade integer, id integer)') # Criando Tabela no banco, campos e tipos

#cursor.execute("INSERT INTO alunos VALUES('"+nome+"', "+str(idade)+", "+str(id)+")") #Inserindo informações través de variaveis

#cursor.execute("DELETE FROM  alunos WHERE idade >= 1") # Deletando informações

#cursor.execute("UPDATE alunos SET id = 177") # Atualizar dados na tabela

# Imprimir os alunos
""" cursor.execute("SELECT * FROM alunos") 
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)
else:
    print () """

# Buscando akuno pelo id
""" cursor.execute("SELECT *FROM alunos WHERE id = 222")
aluno = cursor.fetchone()
if aluno:
    print(f"Nome: {aluno[0]}") # 
else:
    print(f"Aluno com ID {id} não encontrado.")
 """
banco.commit()