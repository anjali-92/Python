from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:////home/anjali/Documents/Python/like_match.sqlite", echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname =  Column(String)
    password =  Column(String)

    def __repr__(self):
        return "<User(name='%s', fullanme='%s', password='%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

session.add(User(name='ed', fullname='Ed Jones', password='edspassword'))
session.add(User(name='ed1', fullname='Ed Jones1', password='edspassword1'))
session.add(User(name='ed12', fullname='Ed Jones2', password='edspassword2'))
session.add(User(name='ed3', fullname='Ed Jones3', password='edspassword3'))
session.commit()

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

print "------------------------"
for row in session.query(User.name).filter( User.name.like('%ed1%')):
    print row
print "------------------------"
import os
os.system("rm like_match.sqlite")
