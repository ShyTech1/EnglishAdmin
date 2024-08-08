import sqlalchemy
from sqlalchemy import create_engine, MetaData, select, insert, update, and_
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from csv_reader import csv_reader_handler as csv_handler

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

# t = s.query(models.Students).all()
# print(t)

# stmt = select(models.Students).join(models.Classes)
# stmt = select(models.Classes)
# result = s.execute(stmt).all()

# print(select(models.Unit_groups))
# for record in result.scalars():
#     print({"id": record.id,
#            "teacher_name": record.teacher_name.strip(),
#            "unit": record.unit.strip(),
#            "unit_group": record.unit_group.strip(),
#            "room": record.room})
# for record in result.scalars():
#     print({"id": record.id,
#            "lname": record.lname.strip(),
#            "fname":record.fname.strip(),
#            "class_id": f"{record.fk_class_id.class_num}+{record.fk_class_id.sub_class}"})
# "unit_group_id": record.unit_group_id.strip()})


# students_data, classes_data = csv_handler()
classes_data = csv_handler()


def add_classes(data):
    s.execute(insert(models.Classes), [{k: v for k, v in vars(i).items() if k[0] != "_"} for i in (list(data))])
    for record in (list(data)):
        class_ = models.Classes(
            class_num=str(record.class_num),
            sub_class=str(record.sub_class),
            educator_name=record.educator_name
        )
        s.add(class_)

    s.commit()


add_classes(classes_data)


def add_students(data):
    classes = s.query(models.Classes.id).filter(and_(
        models.Classes.class_num == '11',
        models.Classes.sub_class == '1'
    )).all()
    class_id = str([i[0] for i in classes][0])

    s.execute(insert(models.Students), [{k: v for k, v in vars(i).items() if k[0] != "_"} for i in (list(data))])
    for record in (list(data)):
        class_ = models.Students(
            lname=record.lname,
            fname=record.fname,
            class_id=class_id,
            module_1=record.module_1,
            module_2=record.module_2,
            literature=record.literature,
            oral=record.oral
        )
        s.add(class_)
    s.commit()


# s.execute(insert(models.Classes),[{k: v for k, v in vars(i).items() if k[0] != "_"} for i in (list(classes_data))])
# for record in (list(classes_data)):
#
#     class_ = models.Classes(
#         class_num=record.class_num,
#         sub_class=record.sub_class,
#         educator_name=record.educator_name
#     )
#     try:
#         s.add(class_)
#     except ValueError:
#         print()
# s.commit()

def print_classes():
    result = s.query(models.Classes).all()
    print(result)
    for record in result:
        print({
            "id": record.id,
            "class_num": record.class_num,
            "sub_class": record.sub_class,
            "educator": record.educator_name.strip()
        })

# for key, value in data.items():
#     print(f"{key} = {value}")
# print(print_classes())
