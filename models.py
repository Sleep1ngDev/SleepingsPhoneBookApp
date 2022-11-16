from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import  relationship
from sqlalchemy import  Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///phones.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = relationship("Phone", cascade='all,delete', back_populates='contact')

    def __str__(self):
        return self.name

    @classmethod
    def add(cls, name):
        contact = cls(name=name)
        session.add(contact)
        session.commit()
        return contact

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)
    contact_id = Column(Integer, ForeignKey('contact.id'))
    contact = relationship("Contact", back_populates='phones')

    @classmethod
    def add(cls, phone, contact):
        phone = cls(phone=phone, contact=contact)
        session.add(phone)
        session.commit()
    def __str__(self):
        return self.name

Base.metadata.create_all(engine)
