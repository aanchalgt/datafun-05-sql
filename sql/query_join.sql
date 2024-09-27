-- query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

SELECT books.year_published,books.title, authors.first, authors.last
FROM authors
JOIN books on authors.author_id = books.author_id;