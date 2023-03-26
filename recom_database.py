import sqlalchemy  # Package for accessing SQL databases via Python

# Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
engine = sqlalchemy.create_engine("postgresql://postgres:jhoncena619@localhost/RB_Recommendation_System")
con = engine.connect()

# Verify that there are no existing tables
print(engine.table_names())

hhre="ENTER Recommendation Date: "
h23="\033[1m" + hhre + "\033[0m"
#fh=h.BOLD()
recom_date=str(input(h23))
BBBB=bbbb.lower()
table_name = f'recom_for_{BBBB}{recom_date}'
fin_results1.to_sql(table_name, con, index=False, if_exists='replace')



print(engine.table_names())

con.close()