-- query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.

SELECT author_id, COUNT(*) AS num_of_books
FROM books
GROUP BY author_id;

SELECT AVG(year_published) AS avg_year_publication
FROM books;