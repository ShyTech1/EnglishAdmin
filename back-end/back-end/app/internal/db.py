from app.database import engine
from sqlalchemy import text

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

def get_scores():
    with engine.connect() as conn:
        # result = conn.execute(text("create schema if not exists test;"))
        # print(result.all())
        result = conn.execute(text("SELECT * from school.scores"))
        return result.all()