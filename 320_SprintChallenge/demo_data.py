# Open a connection to a new (blank) database file demo_data.sqlite3
conn_p1 = sqlite3.connect('demo_data.sqlite3')

# Make a cursor
c_p1 = conn_p1.cursor()

# execute an appropriate CREATE TABLE statement to accept the above data (name the table demo)

c_p1.execute("""
  CREATE TABLE demo (
    s TEXT,
    x INT,
    y INT
  );
""")

# Write and execute appropriate INSERT INTO statements to add the data (as shown above) to the database

c_p1.execute ("""
  INSERT INTO demo (s, x, y)
  VALUES 
    ('v', 5, 9),
    ('g', 3, 9),
    ('f', 8, 7)
  ;
""")

# Verify success
check = c_p1.execute('SELECT * FROM demo;').fetchall()
print(check)

# Count how many rows you have - it should be 3!
c_p1.execute('SELECT COUNT (*) FROM demo').fetchone()[0]

# How many rows are there where both x and y are at least 5?
c_p1.execute("""SELECT COUNT (*)
                FROM demo
                WHERE x > 5
                AND y > 5
             """).fetchall()[0][0] 

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
c_p1.execute("""SELECT COUNT (DISTINCT y)
                FROM demo;
             """).fetchone()[0]

# Close, Commit, Move on
c_p1.close()
c_p1.commit()