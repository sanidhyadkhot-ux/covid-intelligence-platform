WITH vaccination_rollup AS (
    SELECT d.continent, d.location, d.date, d.population, v.new_vaccinations,
    SUM(COALESCE(v.new_vaccinations,0)) OVER (
        PARTITION BY d.location
        ORDER BY d.date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS rolling_vaccinations
    FROM covid_deaths d
    LEFT JOIN covid_vaccinations v
    ON d.location = v.location AND d.date = v.date
    WHERE d.continent IS NOT NULL
)
SELECT *, (rolling_vaccinations / NULLIF(population,0))*100 AS rolling_vaccination_pct
FROM vaccination_rollup;
