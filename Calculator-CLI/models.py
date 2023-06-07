from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database setup
engine = create_engine('sqlite:///calculator.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define the many-to-many association table
calculation_tag_association = Table('calculation_tag_association', Base.metadata,
                                    Column('calculation_id', Integer,
                                           ForeignKey('calculations.id')),
                                    Column('tag_id', Integer,
                                           ForeignKey('tags.id'))
                                    )

# Define the tables


class Calculation(Base):
    __tablename__ = 'calculations'

    id = Column(Integer, primary_key=True)
    operator = Column(String)
    operand1 = Column(Integer)
    operand2 = Column(Integer)
    result = Column(Integer)

    tags = relationship(
        'Tag', secondary=calculation_tag_association, back_populates='calculations')


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    calculations = relationship(
        'Calculation', secondary=calculation_tag_association, back_populates='tags')

    __table_args__ = (
        UniqueConstraint('name', name='uq_name'),
    )


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    calculations = relationship('Calculation', backref='user')


Base.metadata.create_all(engine)

# Database functions


def save_calculation(operator, operand1, operand2, result, tags):
    calculation = Calculation(
        operator=operator, operand1=operand1, operand2=operand2, result=result, tags=tags)
    session.add(calculation)
    session.commit()


def get_all_calculations():
    return session.query(Calculation).all()


def get_calculations_by_tag(tag_name):
    return session.query(Calculation).join(Calculation.tags).filter(Tag.name == tag_name).all()
