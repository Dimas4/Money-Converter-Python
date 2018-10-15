from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from datetime import datetime


Base = declarative_base()


class Money(Base):
    __tablename__ = 'money'

    id = Column(Integer, primary_key=True)
    currency = Column(String)
    price = Column(Float)
    date = Column(String)

    @classmethod
    def update(cls, session, data):
        for value in data:
            timestamp = datetime.strptime(value['Date'][:-9], '%Y-%m-%d').timestamp()
            session.query(cls).filter_by(currency=value['Cur_Abbreviation']) \
                .update({'price': value['Cur_OfficialRate'], 'date': timestamp})

        session.commit()

    def __repr__(self):
        return "<Money({} {})>".format(self.currency, self.price)
