import pyodbc
import pandas as pd

# Connection string (adjust to your setup)
# conn = pyodbc.connect(
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     'SERVER=mssql-179120-0.cloudclusters.net,19289;'
#     'DATABASE=ENGINE;'
#     'UID=admin;'
#     'PWD=nOKIA@520'
# )


def fetch_orders(qry):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=mssql-179120-0.cloudclusters.net,19289;'
        'DATABASE=ENGINE;'
        'UID=admin;'
        'PWD=nOKIA@520'
    )
    query = qry
    df = pd.read_sql(query, conn)
    conn.close()
    return df




def insert_data_sql(qryin):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=mssql-179120-0.cloudclusters.net,19289;'
        'DATABASE=ENGINE;'
        'UID=admin;'
        'PWD=nOKIA@520'
    )
    cursor = conn.cursor()
    cursor.execute(qryin)
    conn.commit()
  # Close connection
    cursor.close()
    conn.close()