SELECT *
FROM news
WHERE tag IN ('#science', '#food')
AND days_gone <= 2
ORDER BY days_gone;