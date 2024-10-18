import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionario"
    
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer, primary_key=True)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Float)
    telefone = Column("telefone", String)
    
    def __init__(self, nome, idade, cpf, setor, funcao, salario, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone
        
# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO)

# Função para limpar a tela
def limpar_tela():
    os.system("cls || clear")

# Função para exibir o menu
def menu():
    print("="*40)
    print(f"{'RH System':^40}")
    print("="*40)
    print("""
    1 - Adicionar um funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário 
    5 - Listar todos os funcionários
    0 - Sair do sistema.     
          """)

# Loop principal do sistema
while True:
    menu()
    opcao = input("Digite o número da opção: ")