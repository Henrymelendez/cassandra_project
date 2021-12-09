# Cassandra Project



# Project Description 


In this project, I applied what I've learned on data modeling with Apache Cassandra and completed an ETL pipeline using Python. To complete the project, I needed to model my data by creating tables in Apache Cassandra to run queries. I was provided, and created an ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

# Things Learned

Designed a NoSQL database using Apache Cassandra based on the original schema outlined in project one. Skills include:

Created a nosql database using Apache Cassandra (both locally and with docker containers)
Developed denormalized tables optimized for a specific set queries and business needs
Proficiencies used: Python, Apache Cassandra, Denormalization


# DataSets

The dataset is contain in csv file in ```/event_data```

```artist, auth, firstName, gender, itemInSession, lastName, length, level, location, method, page, registration, sessionId, song, status, ts, userId```


# Keyspace Schema Design

Data Model ERD
The keyspace design is shown in the image below. Each table is modeled to answer a specific known query. This model enables to query the database schema containing huge amounts of data. Relational databases are not suitable in this scenario due to the magnitude of data.
![alt text](https://github.com/Henrymelendez/cassandra_project/blob/main/keyspace.png)




# ETL

Extract, transform, load (ETL) is the general procedure of copying data from one or more sources into a destination system which represents the data differently from the sources or in a different context than the sources.

Running etl.py first preprocesses the csv file, and then includes Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables. The tables are tested by running SELECT statements.
sql_queries.py contains all SQL queries and is imported into ETL-Pipeline.ipynb.
functions.py contains the preprocessing function that creates new csv files to be used for Apache Cassandra tables and is imported into etl.py
