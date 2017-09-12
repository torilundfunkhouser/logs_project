#!/usr/bin/python3
# This Python file uses the following encoding: utf-8

import psycopg2

# Prints most popular three articles of all time

db = psycopg2.connect(database="news")

cursor1 = db.cursor()
cursor1.execute("""SELECT title FROM slug_title
                GROUP BY title ORDER BY COUNT(title) DESC Limit 3""")
result = cursor1.fetchall()
x = result
print("The top three articles of all time are: %s!" % x)


# Prints the most popular article authors of all time

cursor1 = db.cursor()
cursor1.execute("""SELECT author_name_times.name FROM author_name_times
                GROUP BY author_name_times.name ORDER BY
                COUNT(author_name_times.name) DESC Limit 3
                """)
result = cursor1.fetchall()
x = result
print("The most popular article authors of all time are: %s!" % x)


# Prints the day(s) on which more than 1% of requests lead to errors

cursor1 = db.cursor()
cursor1.execute('SELECT date from error_date')
result = cursor1.fetchall()
print("On this day more than 1% of requests led to errors:")
print(result)
