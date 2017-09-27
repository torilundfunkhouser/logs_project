#! /usr/bin/env python
# This Python file uses the following encoding: utf-8

import psycopg2

db = psycopg2.connect(database="news")


# Returns most popular three articles of all time
def print_top_articles():
    cursor1 = db.cursor()
    cursor1.execute("""SELECT title FROM slug_title
                GROUP BY title ORDER BY COUNT(title) DESC Limit 3""")
    result = cursor1.fetchall()
    print "The most popular articles of all time are: "
    for result in result:
        print "--" + str(result).translate(None, "'[](),")


# Returns most popular three authors of all time
def print_popular_authors():
    cursor1 = db.cursor()
    cursor1.execute("""SELECT author_name_times.name FROM author_name_times
                    GROUP BY author_name_times.name ORDER BY
                    COUNT(author_name_times.name) DESC Limit 3
                    """)
    result = cursor1.fetchall()
    print "The most popular articles of all time are: "
    for result in result:
        print "--" + str(result).translate(None, "'[](),")


# Returns date(s) with more than 1% of GET request errors
def print_error_days():
    cursor1 = db.cursor()
    cursor1.execute('SELECT date from error_date')
    result = cursor1.fetchall()
    print "On this/these date(s) more than 1% of requests returned errors: "
    for result in result:
        print "--" + str(result).translate(None, "'[](),")

# Prints results for each query
if __name__ == '__main__':
    print_top_articles()
    print_popular_authors()
    print_error_days()
