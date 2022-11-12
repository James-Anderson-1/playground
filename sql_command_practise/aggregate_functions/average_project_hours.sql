SELECT project, AVG(hours)
FROM work_sheet
GROUP BY project;


SELECT project, AVG(hours)
FROM work_sheet
GROUP BY project
HAVING avg(hours) > 30;