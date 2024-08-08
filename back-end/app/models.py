import uuid

from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Uuid, Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, MetaData, Enum, text, \
    UniqueConstraint

Base = declarative_base()

class_enum = Enum('9', '10', '11', '12', name='class_num',
                  create_type=False)  # Enum Type: Define the custom enum type unit_enum without creating it directly in the database (create_type=False).
sub_class_enum = Enum('1', '2', '3', '4', '5', '6', '7', name='sub_class_enum', create_type=False)


class Classes(Base):
    __tablename__ = "classes"

    id = Column(Uuid, primary_key=True, server_default=text("uuid_generate_v4()"))
    class_num = Column('class', String)
    sub_class = Column(sub_class_enum)
    educator_name = Column(String)

    __table_args__ = (
        UniqueConstraint('class', 'sub_class', 'educator_name'),
    )

    students = relationship("Students", back_populates="fk_class_id")

    # def __dict__(self):
    #     return {
    #         "class_num": self.class_num,
    #         "sub_class": self.sub_class,
    #         "educator_name": self.educator_name
    #     }


unit_enum = Enum('3', '4', '5', name='unit_enum', create_type=False)


class Unit_groups(Base):
    __tablename__ = "unit_groups"

    id = Column(Uuid, primary_key=True)
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
    id = Column("id", Integer, primary_key=True)
    lname = Column("lname", String)
    fname = Column("fname", String)
    # class_id = Column("class_id", ForeignKey="classes.id")
    class_id = Column("class_id", Uuid, ForeignKey("classes.id"))
    unit_group_id = Column("unit_group_id", ForeignKey("unit_groups.id"))
    # module_1 = Column("module_1", String)
    # module_2 = Column("module_2", String)
    # literature = Column("literature", String)
    # oral = Column("oral", Integer)

    fk_class_id = relationship("Classes", back_populates="students")
    fk_unit_group_id = relationship("Unit_groups", back_populates="students")
