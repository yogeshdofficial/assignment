from sqlalchemy import Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Bank(Base):
    __tablename__ = "banks"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(49))

    branches = relationship("Branch", back_populates="bank")


class Branch(Base):
    __tablename__ = "branches"

    ifsc = Column(String(11), primary_key=True)
    bank_id = Column(BigInteger, ForeignKey("banks.id"))
    branch = Column(String(74))
    address = Column(String(195))
    city = Column(String(50))
    district = Column(String(50))
    state = Column(String(26))

    bank = relationship("Bank", back_populates="branches")


class BankBranchView(Base):
    __tablename__ = "bank_branches"

    ifsc = Column(String(11), primary_key=True)
    bank_id = Column(BigInteger)
    branch = Column(String(74))
    address = Column(String(195))
    city = Column(String(50))
    district = Column(String(50))
    state = Column(String(26))
    bank_name = Column(String(49))
