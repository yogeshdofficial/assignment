to run the program locally

1. first load the data in postgres

```
psql -U postgres
CREATE DATABASE bank;
\q
psql -U postgres -d bank -f sql/seed.sql

```

2. populate .env file

```
mv .env.example .env
```

3. then create a virtual environment and type these

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

I started by understanding the problem and looking at the data that was provided. Since the data was already available as a SQL file, I decided to load it directly into PostgreSQL instead of inserting everything through code. This made it easier to handle a large amount of data.

After importing the data, I checked the database structure and saw that banks and branches were stored in separate tables, with a view that joins both. To keep the API simple, I used this view instead of writing joins in the application code.

For the backend, I used FastAPI because it is simple to set up and gives built-in API documentation. SQLAlchemy ORM is used to map the existing tables and the view so that queries can be written in a clean way. Since the data is static, the ORM is only used for reading data.

Database credentials are taken from environment variables to avoid hardcoding sensitive information. The project is structured in a clean way by separating routes, models, and database configuration.

The API provides endpoints to get the list of banks, get branches for a specific bank, and get branch details using IFSC code. I also added basic test cases to make sure the main endpoints are working.

I've also added test cases that can be ran with

```
pytest
```
