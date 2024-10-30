SELECT
	*
FROM
	job_postings_fact
WHERE
(
	(job_title_short = 'Data Analyst' AND salary_year_avg > 100000)
OR
	(job_title_short = 'Business Analyst' AND salary_year_avg > 70000)
)
AND
	job_location IN ('Boston, MA', 'Anywhere');


SELECT
	*
FROM
	job_postings_fact
WHERE
(
  job_title like '%Data_Analyst%' 
OR
  job_title like '%Business_Analyst%' 
)
AND
	NOT job_title LIKE '%Senior%';