import db_connect as dbc
from settings import DATABASE
import sqlmodel_model as mdl
import sqlmodel_states_insert as sts


if __name__ == "__main__":
    dbc.generic_default_sql(f"CREATE DATABASE {DATABASE};")
    mdl.create_tables()
    sts.insert_states()