SELECT 
  a.name 
FROM employees a
INNER JOIN employees b
ON a.managerID = b.id
