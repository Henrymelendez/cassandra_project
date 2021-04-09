from function import preprocessing
from create_table import *
from sql_queries import *
import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
from cassandra.cluster import Cluster, Session

filepath = os.getcwd() + '/event_data'

preprocessing(filepath)


file = 'event_datafile_new.csv'

def process_file(file,session):
    file = 'event_datafile_new.csv'
    session.execute(drop_table_music)
    session.execute(drop_table_user)
    session.execute(drop_table_song_lib)
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            session.execute(insert_music,(int(line[8]), int(line[3]), line[0], line[9], float(line[5])))
            session.execute(insert_user,(line[0],line[9],int(line[3]),line[1],line[5],int(line[10]),int(line[8])))
            session.execute(song_lib_insert,(line[1],line[4],int(line[10]),line[9]))

        music =session.execute(query1)
        user = session.execute(query2)
        songs = session.execute(query3)

        print(music)
        print(user)
        print(songs)        

if __name__ == '__main__':
    cluster = Cluster()
    session = cluster.connect(['127.0.0.1'])
    

    process_file(file,session)

    
    




            
