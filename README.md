# Udacity Logs Analysis Project
## Overview
For the Udacity Logs Analysis Project, we were asked to connect to build an internal reporting tool using information from a database about a “newspaper site.” The program, which would be run from the command line, had to answer some queries about the website using the database “behind” the site. 

To do this, we had to connect to a database, use SQL queries to analyze the log data, and print out the answers to the questions: 
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

## Setting up the project
1. Install vagrant (https://www.vagrantup.com/) and virtual box (https://www.virtualbox.org/wiki/Downloads) 
2. Download the vagrant configuration files (FSND Virtual Machine - udacity logs projects). Save the folder on your desktop.
3. Download the newsdata.sql file and place it into the vagrant directory
4. cd into your vagrant directory
5. vagrant up
6. vagrant ssh
7. Use the command psql -d news -f newsdata.sql (this creates the database and load the data)

After taking these steps, you should be all set up to start answering the questions.

## Answering the Questions
To answer the first question — What are the most popular three articles of all time? — take the following steps:

*Step 1)* Create a view slug with the times and the slug cut out from the url (i.e. everything after last / ). This will set us up to join the articles table on the slug. 
CREATE VIEW Slug AS
SELECT SUBSTRING(path, 10) as short_path, time from log;

*Step 2)* Create a view slug_title with times, article titles, and slug by joining on the slug.
CREATE VIEW slug_title AS
SELECT Slug.short_path, Slug.time, articles.title
FROM Slug
INNER JOIN articles ON articles.slug=Slug.short_path;

*Step 3)* Run query selecting the titles from the slug_title table, ordered by the count of the article titles accessed most often. Limit 3 to show the top three article titles. 
SELECT title
FROM slug_title
GROUP BY title
ORDER BY COUNT(title) DESC
Limit 3;

To answer the second question — Who are the most popular article authors of all time? — I took the following steps:

*Step 1)* Create a view with author name and slug by joining on author ID from the articles and authors tables.
CREATE VIEW author_name_article AS
SELECT authors.name, articles.slug
FROM articles
INNER JOIN authors ON articles.author=authors.id;

*Step 2)* Create a view with author name and slug, joining on the slug from the new author_name view and logs table. 
CREATE VIEW author_name_times AS 
SELECT author_name_article.name, slug_title.short_path
FROM slug_title
INNER JOIN author_name_article ON slug_title.short_path=author_name_article.slug;

*Step 3)* Run query counting the number of times the path appears in the author_name_times view. Sort by author name with most often seen author on top, then select the top three author names. 
SELECT author_name_times.name
FROM author_name_times
GROUP BY author_name_times.name
ORDER BY COUNT(author_name_times.name) DESC
Limit 3;

Finally, to answer the third question — On which days did more than 1% of requests lead to errors?— I took the following steps:

*Step 1)* Create view errors with columns of counts matched with days where status != 200 OK.
CREATE VIEW errors AS
SELECT count(*) AS COUNT,
       date.day AS date
FROM date
WHERE status!='200 OK'
GROUP BY day
ORDER BY COUNT DESC;

*Step 2)* Create view totals with columns of counts matched with days where status = 200 OK.
CREATE VIEW totals AS 
SELECT count(*) AS COUNT,
       date.day AS date
FROM date
GROUP BY day
ORDER BY COUNT DESC;

*Step 4)* Create view counting the number of days that the percentage of errors (i.e. errors / totals * 100) was greater than 1%.
CREATE VIEW error_date AS
SELECT totals.date, (100.0*errors.count/totals.count) AS percentage
FROM errors, totals
WHERE errors.date=totals.date AND (100.0*errors.count/totals.count) >1
ORDER BY totals.date;

*Step 5)* Run query showing the days from the view created above.
SELECT date from error_date;

## Running the program
To run the program, use python3 news_queries.py






