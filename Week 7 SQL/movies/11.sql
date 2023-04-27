SELECT title
FROM movies, people, stars, ratings
WHERE people.id = stars.person_id
AND movies.id = stars.movie_id
AND movies.id = ratings.movie_id
AND people.name = 'Chadwick Boseman'
ORDER BY ratings.rating DESC LIMIT 5;