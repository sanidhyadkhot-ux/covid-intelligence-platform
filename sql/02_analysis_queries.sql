-- Total cases vs deaths
SELECT location, date, total_cases, total_deaths,
(total_deaths / NULLIF(total_cases, 0)) * 100 AS case_fatality_rate_pct
FROM covid_deaths
WHERE continent IS NOT NULL;

-- Infection rate by country
SELECT location, population, MAX(total_cases) AS highest_cases,
MAX((total_cases / NULLIF(population,0))*100) AS infection_rate_pct
FROM covid_deaths
WHERE continent IS NOT NULL
GROUP BY location, population
ORDER BY infection_rate_pct DESC;
