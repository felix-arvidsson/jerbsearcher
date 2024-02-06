from sqlalchemy import Column, String, Boolean, UniqueConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"
    __table_args__ = (UniqueConstraint('id'),)

    id = Column(String, primary_key=True)
    title = Column(String)
    publishedDate = Column(String)
    email_sent = Column(Boolean)


engine = create_engine('sqlite:///db/jerbs.db')
Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()
session.close()
