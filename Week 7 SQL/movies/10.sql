SELECT DISTINCT name
FROM people, movies, directors, ratings
WHERE people.id = directors.person_id
AND movies.id = directors.movie_id
AND ratings.movie_id = movies.id
AND ratings.rating >= 9.0;