CREATE VIEW vw_covid_intelligence AS
SELECT d.continent, d.location, d.date, d.population,
d.total_cases, d.total_deaths, v.total_vaccinations,
(d.total_cases / NULLIF(d.population,0))*100 AS infection_rate_pct,
(d.total_deaths / NULLIF(d.total_cases,0))*100 AS case_fatality_rate_pct,
(v.total_vaccinations / NULLIF(d.population,0))*100 AS vaccination_coverage_pct
FROM covid_deaths d
LEFT JOIN covid_vaccinations v
ON d.location = v.location AND d.date = v.date
WHERE d.continent IS NOT NULL;
