from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Instanciar Base
Base = declarative_base()

# Criar classe da tabela
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column("nome", String(255))
    email = Column("email", String(255))

    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

# Conexão com bd
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

# Istanciar Session
Session = sessionmaker(bind=engine)
session = Session()

# Add e commitar dados
usuario = Usuario(1, 'fulano', 'fulano@gmail.com')
session.add(usuario)
session.commit()

u2 = Usuario(2, 'ana', 'ana@gmail.com')
u3 = Usuario(3, 'joao', 'joao@gmail.com')

session.add(u2)
session.add(u3)
session.commit()