SELECT
	project_company,
    nerd_role,
	hours_rate AS old_rate,
    hours_rate + 5 AS new_rate,
    hours_spent,
    hours_spent % 8 AS extra_hours
FROM 
	invoices_fact
WHERE
	(new_rate * hours_spent) < 20000
AND
	hours_spent BETWEEN 8 AND 18
AND
	extra_hours > 0
AND 
	NOT project_company = 'Jobs Near Me' 
ORDER BY
	(new_rate * hours_spent + 5) ASC