# Author: Matthew Markwell
# Date: 5/2/2017
#
# Seed the testevergreendb database with some example data for toying with.

import MySQLdb as db


try:
    con = db.connect(user='aaaa', passwd='aaaa', db='testevergreendb', use_unicode=True)
    cur = con.cursor()
    

except:
    print "Failed to create the DB for some reason. Perhaps it already exists?"

