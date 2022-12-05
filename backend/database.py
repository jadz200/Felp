from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://felp_user:rpNkdSc4eyhsimnrPgFCbLm9n4hfQdTh@dpg-ce4a39un6mpku7krloh0-a.frankfurt-postgres.render.com/felp"
SQLALCHEMY_DATABASE_URL = "postgresql://felp_5ubb_user:BQtIpKcSzfzmdMppfE764BT7oX7O7oLI@dpg-ce73dh14rebdt3cu3nig-a.oregon-postgres.render.com/felp_5ubb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
