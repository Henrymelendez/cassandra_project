import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
from function import *
from sql_queries import *
from cassandra.cluster import Cluster, Session

def create_database():
    cluster = Cluster()
    session = cluster.connect(['127.0.0.1:'])

    try:
        session.execute(create_keyspace)
    
    except Exception as e:
        print(e)
    
    try:
        session.set_keyspace('project')
    except Exception as e:
        print(e)
    

    return session, cluster

def drop_database(cluster,session):

    for query in drop_tables:
        session.execute(query)

def create_tables(cluster,session):

    for query in create_table:
        session.execute(query)

def main():

    session, cluster = create_database()

    drop_database(cluster,session)
    create_tables(cluster,session)


if __name__ == '__main__':

    main()

