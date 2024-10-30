SELECT
	*
FROM 
	job_postings_fact
WHERE
	job_country = 'United States' --i love money
AND
	salary_year_avg BETWEEN 250000 AND 300000
AND
	NOT job_via = 'via LinkedIn'
ORDER BY
	salary_year_avg DESC

/*
this query will return all job postings in the United States with an average salary between $250,000 and $300,000, excluding those that were posted via LinkedIn. The results will be ordered by salary in descending order.
*/