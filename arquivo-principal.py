import os
import pandas
from sqlalchemy import create_engine, Column, String, Integer,
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

Base = declarative_base()

class Funcionario(Base):
    __tablename__= "funcionários"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", Integer)
    setor = Column("setor", )
    funcao = Column("função", String)
    salario = Column("saário", )
