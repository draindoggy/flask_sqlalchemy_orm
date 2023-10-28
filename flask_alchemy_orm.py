from sqlalchemy import create_engine, Integer, Column, Text
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('postgresql+psycopg2://postgres:password@127.0.0.1/test') #подключение к базе данных
session = Session(bind=engine)
Base = declarative_base()

class shop_alchemy(Base):
    __tablename__ = 'shop_alchemy'
    id_tovara = Column(Integer(), primary_key=True)
    name = Column(Text)
    price = Column(Text)
    image = Column(Text)

row1 = shop_alchemy(
    id_tovara='1',
    name='New Balance 530 White Silver',
    price='20000',
    image='nb1.jpg'
)

row2 = shop_alchemy(
    id_tovara='2',
    name='Nike Air Force 1 07 White Black',
    price='11500',
    image='airforce1.jpg'
)

row3 = shop_alchemy(
    id_tovara='3',
    name='Adidas Originals Superstar Black',
    price='16000',
    image='adddidas1.jpg'
)

#Base.metadata.create_all(engine)
#session.add(row3)
data_of_name = session.query(shop_alchemy.name).all()
data_of_price = session.query(shop_alchemy.price).all()
data_of_image = session.query(shop_alchemy.image).all()

id_names = [names[0] for names in data_of_name]
text_names = '\n'.join(id_names)

prices = [price[0]for price in data_of_price]
text_prices = '\n'.join(prices)

images = [image[0] for image in data_of_image]
text_images = '\n'.join(images)

print(text_names)
print(text_prices)
print(text_images)
session.commit()