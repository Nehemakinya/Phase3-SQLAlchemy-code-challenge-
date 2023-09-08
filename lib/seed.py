from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

DATABASE_URL = "sqlite:///SQLAlchemycodechallenge.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)

restaurant1 = Restaurant(name="Restaurant 1", price=2)
restaurant2 = Restaurant(name="Restaurant 2", price=3)
customer1 = Customer(first_name="Kelvin", last_name="Hart")
customer2 = Customer(first_name="Ladasha", last_name="Smith")
review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)

session.add(restaurant1)
session.add(restaurant2)
session.add(customer1)
session.add(customer2)
session.add(review1)
session.add(review2)

session.commit()