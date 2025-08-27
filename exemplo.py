from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

## dialetos
## engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

print("Conexão com SQLite estabelecida.")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

#Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

print("Tabela Criada com SQLite estabelecida.")

#Criando uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Adicionar um novo usuário ao banco de dados
try:
    with Session() as session:
        novo_usuario = Usuario(nome="Ana", idade=25)
        session.add(novo_usuario)
        session.commit()   # <-- necessário para gravar no banco
        print("Usuário inserido com sucesso!")
except Exception as e:
    print("Erro:", e)

# Consultar os dados já inseridos
with Session() as session:
    usuarios = session.query(Usuario).all()
    for u in usuarios:
        print(f"ID={u.id}, Nome={u.nome}, Idade={u.idade}")