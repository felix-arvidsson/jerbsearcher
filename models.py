from sqlalchemy import Boolean, Column, String, UniqueConstraint, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"
    __table_args__ = (UniqueConstraint("id"),)

    id = Column(String, primary_key=True)
    title = Column(String)
    publishedDate = Column(String)
    email_sent = Column(Boolean)


engine = create_engine("sqlite:///db/jerbs.db", echo=True)
Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()
session.close()
