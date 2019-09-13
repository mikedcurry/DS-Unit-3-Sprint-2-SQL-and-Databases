##########
# PART 2 #
##########

# Inspect Table Names:
c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()

# What are the ten most expensive items (per unit price) in the database?

c.execute("""SELECT ProductName, UnitPrice
             FROM Product
             ORDER BY UnitPrice DESC
             LIMIT 10;              
          """).fetchall()

c.execute('SELECT BirthDate FROM Employee LIMIT 2;').fetchall()

# What is the average age of an employee at the time of their hiring? 
#   (Hint: a lot of arithmetic works with dates.)

c.execute("""SELECT AVG(2019-09-13 - BirthDate)
             FROM Employee
          """).fetchone()[0]

# Someone ought to call in about all this child labor...

# Maybe come back and figure out why date subtraction looks whack...

##########
# PART 3 #
##########

# What are the ten most expensive items in the database and their suppliers?

c.execute("""SELECT spl.CompanyName, prd.ProductName, prd.UnitPrice
             FROM Product AS prd,
                  Supplier AS spl
             WHERE prd.SupplierID = spl.Id
             ORDER BY prd.UnitPrice DESC
             LIMIT 10;
          """).fetchall()

# Mah ha ha! No use of the JOIN function...

# c.execute("""SELECT spl.CompanyName, prd.ProductName, prd.UnitPrice
#              FROM Supplier AS spl
#              INNER JOIN Product AS prd
#              ON spl.SupplierID = prd.Id
#              ORDER BY prd.UnitPrice DESC
#              LIMIT 10;
#           """).fetchall()

# Sample
# c.execute('SELECT * FROM Supplier').fetchall()[-1]

# Oh Crap, forgot about this...
# c.execute('SELECT sql FROM sqlite_master WHERE name="Supplier";').fetchall()
# Oh man! I read about that stupid Id vs SupplierID things and forgot. Ugh.

# c.execute('SELECT sql FROM sqlite_master WHERE name="Order";').fetchall()

# What is the largest category (by number of unique products in it)?

# c.execute("""SELECT cat.CategoryName, prd.Id, COUNT(*)
#              FROM Product AS prd,
#                   Category AS cat
#              GROUP BY cat.CategoryName   
#              ORDER BY COUNT (*) DESC
#              LIMIT 1;
#           """).fetchone()

# # Hmm... I think I trust the Inner Join for this one...

c.execute("""SELECT cat.CategoryName, prd.Id, COUNT(*)
             FROM Product AS prd
             INNER JOIN Category AS cat
             ON prd.CategoryID = cat.Id
             GROUP BY cat.CategoryName   
             ORDER BY COUNT (*) DESC
             LIMIT 1;
          """).fetchone()

# Close, Commit, Move on
c_p1.close()
c_p1.commit()
