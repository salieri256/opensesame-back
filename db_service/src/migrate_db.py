from sqlalchemy import create_engine
from src.models.user import Base as user_base
from src.models.door import Base as door_base
from src.models.activity_log import Base as activity_log_base
from src.models.lock_log import Base as lock_log_base

DB_URL = '{}://{}:{}@{}:{}/{}'.format('postgresql+psycopg2', 'postgres', 'postgres', 'host.docker.internal', '5432', 'postgres')

engine = create_engine(DB_URL, echo=True)

def reset_detabase():
    user_base.metadata.drop_all(bind=engine)
    user_base.metadata.create_all(bind=engine)

    door_base.metadata.drop_all(bind=engine)
    door_base.metadata.create_all(bind=engine)

    activity_log_base.metadata.drop_all(bind=engine)
    activity_log_base.metadata.create_all(bind=engine)
    
    lock_log_base.metadata.drop_all(bind=engine)
    lock_log_base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    reset_detabase()