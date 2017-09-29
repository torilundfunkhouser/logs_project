#!/usr/bin/python3
# This Python file uses the following encoding: utf-8

import psycopg2

db = psycopg2.connect(database="news")


# Returns most popular three articles of all time
def print_top_articles():
    cursor1 = db.cursor()
    cursor1.execute("""SELECT * from articles_count limit 3""")
    result1 = cursor1.fetchall()
    print "The the most popular articles of all time are: "
    for (count, title) in result1:
        print str(title).translate(None, "'[](),") + \
            " -- " + str(count).translate(None, "'[](),") + " views"


# Returns most popular three authors of all time
def print_popular_authors():
    cursor1 = db.cursor()
    cursor1.execute("""SELECT * from authors_count limit 3""")
    result2 = cursor1.fetchall()
    print "The the most popular articles of all time are: "
    for (count, name) in result2:
        print str(name).translate(None, "'[](),") + \
            " -- " + str(count).translate(None, "'[](),") + " views"


# Returns date(s) with more than 1% of GET request errors
def print_error_days():
    cursor1 = db.cursor()
    cursor1.execute("""SELECT * from error_date""")
    result3 = cursor1.fetchall()
    print "On this/these date(s) more than 1% of requests returned errors: "
    for (date, percentage) in result3:
        print str(date).translate(None, "'[](),") + \
            " -- " + str(round(percentage, 2)).translate(None, "'[](),") + " %"

# Prints results for each query
if __name__ == '__main__':
    print_top_articles()
    print_popular_authors()
    print_error_days()
