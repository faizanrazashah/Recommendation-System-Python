startTime = time.time()
import psycopg2
conn = psycopg2.connect(host="localhost", port = 5432, database="RB_Recommendation_System", user="postgres", password="jhoncena619")
cur = conn.cursor()
def create_pandas_table(sql_query, database = conn):

    table = pd.read_sql_query(sql_query, database)

    return table

T_frames = create_pandas_table("SELECT * FROM rbpre ")

import datetime
T_frames['Invoice_Date']=pd.to_datetime(T_frames['Invoice_Date'],format='%Y%m%d')

print(T_frames)
print(T_frames.dtypes)

print(T_frames.isnull().sum())

cur.close()

conn.close()

print ('The script took {0} second !'.format(time.time() - startTime))