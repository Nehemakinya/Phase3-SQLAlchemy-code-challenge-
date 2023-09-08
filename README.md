## SQLAlchemy Restaurant Review System

This is a simple restaurant review system implemented using SQLAlchemy, a powerful Object-Relational Mapping (ORM) library for Python. This system includes the following components:

Database Schema: Defining the structure of the database using SQLAlchemy models.
Migrations: Managing database schema changes using Alembic.
Seed Data: Populating the database with initial sample data.
Object Relationship Methods: Implementing methods to manage relationships between Restaurant, Customer, and Review objects.
Aggregate and Relationship Methods: Calculating aggregate values and handling relationships between objects.

## Prerequisites

Before getting started, ensure you have the following dependencies installed:

--Python (version 3.6 or higher)
--SQLAlchemy
--Alembic (for managing database migrations)
You can install the required dependencies using pip:

    pip install sqlalchemy alembic

## Setup

Clone this repository to your local machine:
     git clone <repository-url>
     cd sqlalchemy-restaurant-review
Update the DATABASE_URL in the code to point to your SQLite database file:

## In models.py, seeds.py, and any other relevant files

DATABASE_URL = "sqlite:///SQLAlchemycodechallenge.db"
Initialize the Alembic migrations:
    alembic init alembic

Edit the alembic.ini file to set your database URL.
Generate the initial migration:
   alembic revision --autogenerate -m "Initial migration"

Edit the generated migration script in the 'alembic/versions' directory to create the 'reviews' table and establish relationships between tables. An example migration script has been provided in this repository as a reference.
Run the migration to create the database tables:
    alembic upgrade head

## Usage

## Seed Data

To populate the database with sample data, run the seeds.py script:
    python seeds.py

This script creates instances of Restaurant, Customer, and Review classes and adds them to the database.

## Object Relationship Methods

The SQLAlchemy models (Restaurant, Customer, Review) include various methods to manage object relationships. For example:

Restaurant.reviews(): Returns all reviews for a restaurant.
Customer.restaurants(): Returns all restaurants reviewed by a customer.

## Aggregate and Relationship Methods

You can use additional methods to perform operations such as calculating the fanciest restaurant or finding a customer's favorite restaurant. For example:

Restaurant.fanciest(): Returns the restaurant with the highest price.
Customer.favorite_restaurant(): Returns the customer's favorite restaurant based on the highest review rating.

## Running Custom Queries

You can use SQLAlchemy's query methods to perform custom queries and retrieve data as needed for your restaurant review system.

## Contributing

Contributions to this project are welcome. Feel free to open issues or pull requests to suggest improvements or report problems.

## Acknowledgments
SQLAlchemy: https://www.sqlalchemy.org/
Alembic: https://alembic.sqlalchemy.org/



