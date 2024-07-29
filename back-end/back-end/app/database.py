from sqlalchemy import create_engine, MetaData, select, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app import models

# Create the SQLAlchemy engine
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
CONNECTION_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
# this might be the correct way to refer to postgres database with the specific port.

SCHEMA_NAME = "school"

engine = create_engine(CONNECTION_DATABASE_URL,
                       connect_args={'options': f'-csearch_path={SCHEMA_NAME}'})

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a Base class
# this function returns a class
# we will inherit from this class to create
# each of the database models or classes (the ORM models)

s = SessionLocal()

# t = s.query(models.Classes).all()
# for record in t:
#     print({"id": record.id, "class": record.class_num, "sub_class": record.sub_class, "educator": record.educator_name})

t = s.query(models.Students).all()

# print(t)

stmt = select(models.Students)
result = s.execute(stmt)
print(result)

for record in result.scalars():
    print({"id": record.id,
           "lname": record.lname.strip(),
           "fname":record.fname.strip(),
           # "class_num": record.class_num,
           "teacher_id": record.teacher_id,
           "class_id": record.class_id,
           "unit_group_id": record.unit_group_id.strip()})

# query = insert(models.Students).values(id=312560626,
#                                        lname="Kelman",
#                                        fname="Cherut",
#                                        teacher_id="f84ba710-40e3-4273-b77e-63660ee541f5",
#                                        class_id=)
