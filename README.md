# Cassandra Project


#Project Description 


In this project, I applied what I've learned on data modeling with Apache Cassandra and completed an ETL pipeline using Python. To complete the project, I needed to model my data by creating tables in Apache Cassandra to run queries. I was provided, and created an ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.


#DataSets

The dataset is contain in csv file in ```/event_data```


#ETL

Extract, transform, load (ETL) is the general procedure of copying data from one or more sources into a destination system which represents the data differently from the sources or in a different context than the sources.

Running etl.py first preprocesses the csv file, and then includes Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables. The tables are tested by running SELECT statements.
sql_queries.py contains all SQL queries and is imported into ETL-Pipeline.ipynb.
functions.py contains the preprocessing function that creates new csv files to be used for Apache Cassandra tables and is imported into etl.py
