from sqlalchemy import create_engine
from src.models.user import Base

DB_URL = '{}://{}:{}@{}:{}/{}'.format('postgresql+psycopg2', 'postgres', 'postgres', 'db', '5432', 'db')

engine = create_engine(DB_URL, echo=True)

def reset_detabase():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    reset_detabase()