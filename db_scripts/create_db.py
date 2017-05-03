# Author: Matthew Markwell
# Date: 5/2/2017
# 
# This file creates a new MySQL database.
# By default it will call the database 'testevergreendb'.
# Optionally, a database name can be passed in from the command line.
# The evergreendb tables are created in this new database.
#
# This is not production code - it is just a way to construct 
# the database for testing. The production version should probably
# use the flask mysql API and have much better error handling.

import MySQLdb as db
import sys

db_name = "testevergreendb"
if (len(sys.argv) > 1):
    db_name = sys.argv[1]


# Create the database if it doesn't exist
con = db.connect(user='aaaa', passwd='aaaa', use_unicode=True)
cur = con.cursor()
create_cmd = "CREATE DATABASE IF NOT EXISTS %s" % db_name
cur.execute(create_cmd)

con = db.connect(user='aaaa', passwd='aaaa', db=db_name, use_unicode=True)
cur = con.cursor()
cur.execute("""CREATE TABLE Children(
            ID CHAR(16) NOT NULL,
            EnglishName VARCHAR(255) NOT NULL,
            ChineseName VARCHAR(255),
            PinyinName VARCHAR(255),
            Nickname VARCHAR(255),
            Sex CHAR(1),
            DOB DATE,
            ChildPhoto BLOB,
            AbandonmentDate DATE,
            ProgramEntryDate DATE,
            ProgramDepartureDate DATE,
            ProgramDepartureReason TEXT,
            ChildHistory TEXT,
            IsActive BOOL,
            MedicalHistory TEXT,
            PRIMARY KEY ( ID ))""")
