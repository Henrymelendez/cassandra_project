
create_keyspace = """CREATE KEYSPACE IF NOT EXISTS udacity WITH REPLICATION =
    {'class':'SimpleStrategy', 'replication_factor':1};"""

drop_table_music = """DROP TABLE IF EXISTS music"""
drop_table_user = """DROP TABLE IF EXISTS user"""
drop_table_song_lib= """DROP TABLE IF EXISTS song_lib"""


# Create tablea
music_table = """CREATE TABLE IF NOT EXISTS music (sessionid int, iteminsession int, 
artist_name text, song text, length float, 
PRIMARY KEY(sessionid, iteminsession))"""

user_table = """CREATE TABLE users (artist text, song text, iteminsession int, fisrtName text,lastName text, 
userid int, sessionid int, PRIMARY KEY((userid,sessionid),iteminsession))"""

song_lib_table = """"CREATE TABLE IF NOT EXISTS song_lib (firstName text, lastName text, 
    userid int, song text, PRIMARY KEY((song), userid))"""

# insert data into tables

insert_music = """INSERT INTO music (sessionid, iteminsession, artist_name, song, length) 
        VALUES (%s, %s, %s, %s, %s)"""

insert_user = """INSERT INTO users (artist, song, iteminsession, fisrtName, lastName, userid, sessionid)
        VALUES (%s,%s,%s,%s,%s,%s,%s)"""

song_lib_insert = """INSERT INTO song_lib (firstName, lastName, userid, song)
        VALUES (%s,%s,%s,%s)"""

query1 = """SELECT * FROM music WHERE sessionid = 338 AND iteminsession = 4"""

query2 = """SELECT artist, song, fisrtName, lastName FROM users WHERE userid = 10 AND sessionid = 182"""

query3 = "SELECT firstName, lastName FROM song_lib WHERE song = 'All Hands Against His Own'"



drop_tables = [drop_table_user,drop_table_music,drop_table_song_lib]
create_table = [music_table,user_table,song_lib_table]