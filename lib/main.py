from setup import session
from models import Restaurant, Customer, Review

restaurants = session.query(Restaurant).all()
for restaurant in restaurants:
    print(restaurant.name)

customer = session.query(Customer).filter_by(first_name="John").first()
favorite = customer.favorite_restaurant()
print(f"{customer.full_name()}'s favorite restaurant is {favorite.name}")

new_review = Review(restaurant=favorite, customer=customer, star_rating=4)
session.add(new_review)
session.commit()

restaurant_to_delete_reviews = session.query(Restaurant).filter_by(name="Restaurant B").first()
customer.delete_reviews(restaurant_to_delete_reviews)

fanciest = Restaurant.fanciest()
print(f"The fanciest restaurant is {fanciest.name}")
