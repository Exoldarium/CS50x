SELECT name
FROM movies, people, stars
WHERE people.id = stars.person_id
AND movies.id = stars.movie_id
AND title = 'Toy Story';