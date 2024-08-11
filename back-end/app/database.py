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

students_data, classes_data = csv_handler()


def add_classes(data):
    # s.execute(insert(models.Classes), [{k: v for k, v in vars(i).items() if k[0] != "_"} for i in (list(data))])

    try:
        # Convert data to a list to ensure it's iterable
        data_list = list(data)

        # Iterate through each record in the data
        for record in data_list:
            # Create a new instance of the Classes model
            class_ = models.Classes(
                class_num=str(record.class_num),  # Convert to string if necessary
                sub_class=str(record.sub_class),
                educator_name=record.educator_name
            )
            # Add the instance to the session
            s.add(class_)

        # Commit the transaction
        s.commit()
        print(f"Added {len(data_list)} records successfully.")

    except Exception as e:
        # Rollback the transaction in case of an error
        s.rollback()  # If an exception occurs, s.rollback() is called to undo any changes made during the transaction.
        print(f"An error occurred: {e}")

    # finally:
    # Optional: Close the session if necessary
    # s.close()


# add_classes(classes_data)


def add_students(data):
    try:
        # Iterate through each record in the data
        for record in data:
            # Query the class UUID based on class_num and sub_class
            class_uuid = s.query(models.Classes.id).filter(and_(
                models.Classes.class_num == record["class_num"],
                models.Classes.sub_class == record["sub_class"]
            )).all()[0][0]

            # Create a new instance of the Students model
            student_ = models.Students(
                id=record["id"],
                lname=record["lname"],
                fname=record["fname"],
                class_id=class_uuid,
                module_1=record["module_1"],
                module_2=record["module_2"],
                literature=record["literature"],
                oral=record["oral"]
            )
            # Add the instance to the session
            s.add(student_)

        # Commit the transaction
        s.commit()
        print(f"Added {len(data)} student records successfully.")

    except Exception as e:
        # Rollback the transaction in case of an error
        s.rollback()
        print(f"An error occurred: {e}")


# add_students(students_data)

def add_unit_group(data):
    pass


def print_classes():
    result = s.query(models.Classes).all()
    for record in result:
        print({
            "id": record.id,
            "class_num": record.class_num,
            "sub_class": record.sub_class,
            "educator": record.educator_name.strip()
        })


def print_students():
    result = s.query(models.Students).all()
    for record in result:
        print({
            "id": record.id,
            "lname": record.lname.strip(),
            "fname": record.fname.strip(),
            "class_id": record.class_id,
            "module_1": record.module_1,
            "module_2": record.module_2,
            "literature": record.literature,
            "oral": record.oral
        })



