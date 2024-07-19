from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Uuid, Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, MetaData


Base = declarative_base()
class Classes(Base):
    __tablename__ = "classes"
    id = Column(Uuid, primary_key=True)
    class_num = Column('class', Integer) #take note name pos allows to use a preserved name of python
                                                    # !!! it's actually says,select class as class_num
    sub_class = Column(Integer)
    educator_name = Column(String(255))

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
