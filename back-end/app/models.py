import uuid

from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Uuid, Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, MetaData, Enum, text, \
    UniqueConstraint

Base = declarative_base()

class_enum = Enum('ט', 'י', 'יא', 'יב', name='class_num',
                  create_type=False)  # Enum Type: Define the custom enum type unit_enum without creating it
# directly in the database (create_type=False).


sub_class_enum = Enum('1', '2', '3', '4', '5', '6', '7', name='sub_class_enum', create_type=False)


class Classes(Base):
    __tablename__ = "classes"

    id = Column(Uuid, primary_key=True, server_default=text("gen_random_uuid()"))
    class_num = Column('class', String)
    sub_class = Column(sub_class_enum)
    educator_name = Column(String)

    __table_args__ = (
        UniqueConstraint('class', 'sub_class', 'educator_name'),
    )

    students = relationship("Students", back_populates="fk_class_id")


unit_enum = Enum('3', '4', '5', name='unit_enum', create_type=False)


class Unit_groups(Base):
    __tablename__ = "unit_groups"

    id = Column(Uuid, primary_key=True, server_default=text("gen_random_uuid()"))
    teacher_name = Column(String)
    unit = Column(unit_enum)
    unit_group = Column(String)
    room = Column(String)

    students = relationship("Students", back_populates="fk_unit_group_id")


class Students(Base):
    __tablename__ = "students"
    # deleted_at | timestamp without time zone
    # created_at | timestamp without time zone
    # updated_at | timestamp without time zone
    id = Column(Integer, primary_key=True)
    lname = Column(String)
    fname = Column(String)
    class_id = Column(Uuid, ForeignKey("classes.id"))
    unit_group_id = Column(ForeignKey("unit_groups.id"))
    module_1 = Column(String)
    module_2 = Column(String)
    literature = Column(String)
    oral = Column(Integer)

    fk_class_id = relationship("Classes", back_populates="students")
    fk_unit_group_id = relationship("Unit_groups", back_populates="students")
    fk_module_1 = relationship("Module_1", back_populates="students")


class Module_1(Base):
    __tablename__ = "module_1"


    id = Column(Uuid, primary_key=True, server_default=text("gen_random_uuid()"))
    student_id = Column(Integer, ForeignKey("students.id", name='fk_module_1'))
    module_name = Column(String)
    notes = Column(String)
    season = Column(String)
    accommodations = Column(String)
    mock_1 = Column(Integer)
    mock_2 = Column(Integer)
    performance = Column(Integer)
    attendance = Column(Integer)
    bagrut_grade = Column(Integer)
    annual_grade = Column(Integer)
    final_module_grade = Column(Integer)

    students = relationship("Students", back_populates="fk_module_1")
