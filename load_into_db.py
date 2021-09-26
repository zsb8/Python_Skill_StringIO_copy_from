from io import StringIO
from utils import pgfunctions as pg
import pandas as pd

def df_to_dt(table, columns, df):
    output = StringIO()
    df.to_csv(output, index=False, header=False, mode="a",
              sep=";")
    f = StringIO(output.getvalue())  # Read from RAM
    conn = pg.connect()
    cursor = conn.cursor()
    cursor.copy_from(f, table, sep=";", columns=columns)
    conn.commit()
    cursor.close()
    conn.close()
    output.truncate() # Don't forget to clear the data


data = [
      {"a":1,"b":5,"c":8},
      {"a":2,"b":6,"c":9},
      {"a":3,"b":7,"c":10}
      ]
index = [0,1,2]
columns = ["a","b","c"]
df = pd.DataFrame(data, index, columns)
print(f"test data set is :\n{df}")



table = "test"
columns = ['a', 'b', 'c']
df_to_dt(table, columns, df)
print("Complete loading into DB by StingIO and copy_from.")
