import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

MEU_BANCO = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind=MEU_BANCO)
session = Session()
lista_funcionario = []

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

def limpar_tela():
    os.system("cls || clear")

def menu():
    print("""
    1 - Adicionar um funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário 
    5 - Listar todos os funcionários
    0 - Sair do sistema.     
          """) 
    
while True:
    menu()
    opcao = input("Digite um número: ")
    match opcao:
        case "1":
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            cpf_funcionario = int(input("Digite seu CPF: "))
            setor = int(input("Digite seu setor: "))
            funcao = input("Digite sua função: ")
            salario = int(input("Digite seu salário: "))
            telefone = int(input("Digite seu telefone: "))

        case "2":
            cpf_funcionario = int(input("Digite seu CPF: "))
            lista_funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()
            for funcionario in lista_funcionario:
                print(f"{funcionario.id} - {funcionario.nome} - {funcionario.idade} - {funcionario.cpf} - {funcionario.setor} - {funcionario.funcao} - {funcionario.salario} - {funcionario.telefone}")
            limpar_tela()

        case "3":
            cpf_funcionario = int(input("Digite seu CPF: "))
            funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()

            novos_dados = Funcionario(
            nome = input("Digite seu nome: "),
            idade = int(input("Digite sua idade: ")),
            cpf_funcionario = int(input("Digite seu CPF: ")),
            setor = input("Digite seu setor: "),
            funcao = input("Digite sua função: "),
            salario = float(input("Digite seu salário: ")),
            telefone = int(input("Digite seu telefone: "))
            )

            funcionario = novos_dados
            session.add(funcionario)
            session.commit
            print("Funcionário atualizado.")
            limpar_tela()

        case "4":
            cpf_funcionario = int(input("Digite o CPF: "))
            funcionario = session.query(Funcionario).filter_by(cpf = cpf_funcionario).first()
            session.delete(funcionario)
            session.commit()
            print("Funcionário excluído.")
            limpar_tela()

        case "5":
            limpar_tela()
        
        case "0":
            break