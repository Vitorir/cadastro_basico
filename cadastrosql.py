from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Usuario

engine = create_engine('mysql://Vitor75123:senha@localhost/cadastro')
