import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

MEU_BANCO = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind=MEU_BANCO)
session = Session()

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionario"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer)
    setor = Column("setor", Integer)
    funcao = Column("funcao", String)
    salario = Column("salario", Integer)
    telefone = Column("telefone", Integer)

    def __init__(self, nome: str, idade: int, cpf: int, setor: int, funcao: str, salario: int, telefone: int):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

Base.metadata.create_all(bind=MEU_BANCO)

os.system("cls || clear")

print("Solicitandos dados para o funcionário")
inserir_nome = input("Digite o seu nome: ")
inserir_idade = int(input("Digite sua idade: "))
inserir_cpf = int(input("Digite o seu CPF: "))
inserir_setor = int(input("Digite o seu setor: "))
inserir_funcao = input("Digite sua função: ")
inserir_salario = int(input("Digite seu salário: "))
inserir_telefone = int(input("Digite seu telefone: "))

funcionario = Funcionario(nome=inserir_nome, idade=inserir_idade, cpf=inserir_cpf, setor=inserir_setor, funcao=inserir_funcao, salario=inserir_salario, telefone=inserir_telefone)
session.add(funcionario)
session.commit()

print("\nExcluindo um funcionário.")
cpf_funcionario = int(input("Informe o CPF do funcionário para ser exlcuído: "))

funcionario = session.query(funcionario).filter_by(cpf = cpf_funcionario).first()
session.delete(funcionario)
session.commit()
print("Funcionário excluído com sucesso.")

print("\nExibindo todos os funcionários do banco de dados.")
lista_funcionarios = session.query(Funcionario).all()

for funcionario in lista_funcionarios:
    print(f"{funcionario.id} - {funcionario.nome} - {funcionario.idade} - {funcionario.cpf} - {funcionario.setor} - {funcionario.funcao} - {funcionario.salario} - {funcionario.telefone}")

print("\nAtualizando dados do funcionário.")
funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()

novos_dados =  Funcionario(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    cpf = int(input("Digite seu CPF: ")),
    setor = int(input("Digite seu setor: ")),
    funcao = input("Digite sua função: "),
    salario = int(input("Digite seu salário: ")),
    telefone = int(input("Digite seu telefone: "))
)

funcionario = novos_dados
session.add(funcionario)
session.commit()

session.close()