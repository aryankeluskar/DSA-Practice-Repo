SELECT
	job_title,
    job_location,
    COUNT(job_title) AS jobs_available,
    AVG(salary_year_avg) AS avg_salary
FROM
	job_postings_fact
GROUP BY
	job_title
HAVING
	jobs_available > 100
    AND
    avg_salary > 100000
ORDER BY
	avg_salary DESC