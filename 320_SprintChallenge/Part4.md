### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?
  - The relationship between `Territory` and `Employee` are established first by the primary key of `Territory` matching the foreign key of the `EmployeeTerritory`, then matching the primary keys of both `Employee` and `EmployeeTerritory`. This an instance of a one to many relationship: the one TerritoryIDs to many EmployeeIDs, presuposing that there is more than one employee per territory (see Jason Murphy alone in Mississippi).

- What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
    - MongoDB is a database for very large datasets built on NoSQL style format. It is document-oriented, which means that it is basically composed of a ton of dictionaries. This sort of unstructed database is suited for the "dumping everything into the soup" model, where you take all kinds / sources of data prior to ordering it into preconceived structure and use it to look for patterns. 


- What is "NewSQL", and what is it trying to achieve?
    - There are different advantages to structed vs unstructed databases. NewSQL is essentially an attempt to find a way to combine both sets of advantages. You want all the minability of the big soup-pot of NoSQL, but the reliability of regular-SQL. Particullartly, NewSQL hopes to find a way to prevent issues with consistency in sequenced database queries, where you want to make sure that one change does not conflict with another. 