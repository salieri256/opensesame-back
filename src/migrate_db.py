from sqlalchemy import create_engine
from src.models.user import Base as user_base
from src.models.log import Base as log_base

DB_URL = '{}://{}:{}@{}:{}/{}'.format('postgresql+psycopg2', 'postgres', 'postgres', 'db', '5432', 'db')

engine = create_engine(DB_URL, echo=True)

def reset_detabase():
    user_base.metadata.drop_all(bind=engine)
    user_base.metadata.create_all(bind=engine)
    log_base.metadata.drop_all(bind=engine)
    log_base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    reset_detabase()