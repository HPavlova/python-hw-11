from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from src.__init__ import app, db


class Contact(db.Model):
    __tablename__ = "contacts"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = relationship("Phone", cascade="all, delete-orphan", back_populates="contact")
    email = relationship("Email", cascade="all, delete-orphan", back_populates="contact")

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Phone(db.Model):
    __tablename__ = "phones"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50), nullable=True, default='No phone')
    contact_id = db.Column(db.Integer, ForeignKey('contacts.id'), nullable=False)
    contact = relationship("Contact", back_populates="phone")


class Email(db.Model):
    __tablename__ = "emails"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=True, default='No email')
    contact_id = db.Column(db.Integer, ForeignKey('contacts.id'), nullable=False)
    contact = relationship("Contact", back_populates="email")


if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    