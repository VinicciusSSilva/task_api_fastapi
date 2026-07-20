from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Banco SQLite será criado automaticamente
DATABASE_URL = "sqlite:///./tasks.db"

# Conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Sessão do banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para os modelos
Base = declarative_base()

# Dependência para usar nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()