-- query_sorting.sql - use ORDER BY to sort data.

Select DISTINCT *
FROM authors
ORDER BY first ASC;

SELECT * 
FROM books
ORDER BY year_published DESC;
