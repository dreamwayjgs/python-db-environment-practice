from typing import List
import psycopg2 as pg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from models_gen import User
from models_dataclass import User


def connect_and_query():
    pgsql_connection = pg.connect(
        host="postgres", password="1234", user="postgres", database="project"
    )
    cur = pgsql_connection.cursor()
    cur.execute('select * from "User"')

    print(cur.fetchone())

    pgsql_connection.close()


def sqlalchemy_connect_and_query():
    engine = create_engine("postgresql://postgres:1234@postgres/project")

    Session = sessionmaker(bind=engine)
    session = Session()
    # new_user = User(name="abc", password="bcd")
    # session.add(new_user)
    # session.commit()

    # new_user = User("abcdd", "eed")
    # session.add(new_user)
    # session.commit()

    result: List[User] = session.query(User).all()
    for row in result:
        print(row.id, row.name, row.password)

    # with engine.connect() as conn:
    #     result = conn.execute('select * from "User"')
    #     for row in result:
    #         print(row)
