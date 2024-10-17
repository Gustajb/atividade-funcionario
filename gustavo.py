print("Solicitando dados para o usuário")

inserir_nome = input("Digite seu nome: ")
inserir_idade = int(input("Digite sua idade: "))
inserir_cpf = int(input("Digite seu cpf: "))
inserir_setor = int(input("Digite seu setor: "))
inserir_funcao = input("Digite sua função: ")
inserir_salario = int(input("Digite seu salãrio: "))
inserir_telefone = int(input("Digite seu telefone: "))

funcionario = Funcionario(nome=inserir_nome, idade=inserir_idade, cpf=inserir_cpf, setor=inserir_setor, 
funcao=inserir_funcao, salario=inserir_salario, telefone=inserir_telefone )
session.add(funcionario)
session.commit()

# Delete
print("\nExcluindo um funcionário.")
email_usuario = input("Informe o cpf do usuário para ser excluído:")

funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()
session.delete(funcionario)
session.commit()
print("Funcionário excluido com sucesso.")

# Listando todos os usuários do banco de dados.
print("\nExibindo todos os usuários do banco de dados")
lista_funcionarios = session.query(Funcionario).all()

# Read
for funcionario in lista_funcionarios:
   print(f"{funcionario.id} - {funcionario.nome} - {funcionario.idade} - {funcionario.cpf} - 
         {funcionario.setor} - {funcionario.funcao} - {funcionario.salario} - {funcionario.telefone}")

# Update.
print("\nAtualizando dados do usuário.")
usuario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()

novos_dados = Funcionario(
    print("Solicitando dados para o usuário")
    inserir_nome = input("Digite seu nome: ")
    inserir_idade = int(input("Digite sua idade: "))
    inserir_cpf = int(input("Digite seu cpf: "))
    inserir_setor = int(input("Digite seu setor: "))
    inserir_funcao = input("Digite sua função: ")
    inserir_salario = int(input("Digite seu salãrio: "))
    inserir_telefone = int(input("Digite seu telefone: "))
)
funcionario = Funcionario(nome=inserir_nome, idade=inserir_idade, cpf=inserir_cpf, setor=inserir_setor, 
                          funcao=inserir_funcao, salario=inserir_salario, telefone=inserir_telefone)
session.add(usuario)
session.commit()

funcionario = novos_dados
session.add(funcionario)
session.commit()

# Fechando conexão.
session.close()

