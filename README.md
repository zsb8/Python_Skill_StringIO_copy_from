# Python_StringIO_copy_from

About SringIO : Read and write str in memory. To write str to StringIO, we need to create a StringIO first, and then write it like a file.

About copy_from : Use copy_from to make the temp_file format and columns have the same column order and name. The introduction of high speed comes at the expense of flexibility.

~~~python
    output = StringIO()
    df.to_csv(output, index=False, header=False, mode="a", sep=";")
    f = StringIO(output.getvalue())
    conn = pg.connect()
    cursor = conn.cursor()
    cursor.copy_from(f, table, sep=";", columns=columns)
~~~
