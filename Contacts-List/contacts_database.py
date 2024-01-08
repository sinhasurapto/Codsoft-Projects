from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import String
from sqlalchemy import create_engine
from user_interface import *


# Declarative base class
class Base(DeclarativeBase):
    pass


# Contacts class
class Contacts(Base):
    __tablename__ = "Contacts"
    contact_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40))
    phone: Mapped[str] = mapped_column(String(10))
    email_id: Mapped[str] = mapped_column(String(30))
    city: Mapped[str] = mapped_column(String(20))


# Connections for the database
engine = create_engine("sqlite+pysqlite:///my_database.db", echo=True)
session = Session(autoflush=False, bind=engine)

# Start the database
Base.metadata.create_all(engine)


# Add contact to the database
def add_contact(c_name, c_phone, c_email, c_city):
    new_contact = Contacts(name=c_name, phone=c_phone, email_id=c_email, city=c_city)
    session.add(new_contact)
    session.commit()


# Delete contact from the database
def delete(del_obj):
    session.delete(del_obj)
    session.commit()


# View contact details of a person
def contact_details(name):
    search_obj = session.query(Contacts).filter_by(name=name).first()
    return search_obj


# Updation of contact of a person
def edit_contact(update_obj, c_name, c_phone, c_email, c_city):
    update_obj.name = c_name
    update_obj.phone = c_phone
    update_obj.email_id = c_email
    update_obj.city = c_city
    session.commit()


# Return list of contacts
def view_contacts():
    contacts = session.query(Contacts).order_by(Contacts.name.asc()).all()
    return contacts
