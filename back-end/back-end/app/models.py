
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Uuid, Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, MetaData

Base = declarative_base()


class Classes(Base):
    __tablename__ = "classes"
    id = Column(Uuid, primary_key=True)
    class_num = Column('class', Integer)  # take note name pos allows to use a preserved name of python
    # !!! it's actually says,select class as class_num
    sub_class = Column(Integer)
    educator_name = Column(String(255))

    fk_student_id = relationship("Students", back_populates="fk_class_id"
                                                            "")

class Students(Base):
    __tablename__ = "students"
    # deleted_at | timestamp without time zone
    # created_at | timestamp without time zone
    # updated_at | timestamp without time zone
    id = Column("id", Integer, primary_key=True)
    lname = Column("lname",String)
    fname = Column("fname", String)
    teacher_id = Column("teacher_id", Integer)
    class_id = Column("class_id", Uuid, ForeignKey("classes.id"))
    unit_group_id = Column("unit_group_id", String)

    fk_class_id = relationship("Classes", back_populates="fk_student_id")


# return to create relationships section.


# class Teachers(Base):
#     __tablename__ = "teachers"
#
#     id = Column(Integer, primary_key=True)
#     fname = Column(String(255))
#     lanme = Column(String(255))
#     created_at = Column(TIMESTAMP)
#     updated_at = Column(TIMESTAMP)
#     deleted_at = Column(TIMESTAMP)
#
#     owner = relationship("User", back_populates="items")
