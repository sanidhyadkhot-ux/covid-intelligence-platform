CREATE TABLE covid_deaths (
    iso_code VARCHAR(10),
    continent VARCHAR(100),
    location VARCHAR(100),
    date DATE,
    population BIGINT,
    new_cases FLOAT,
    total_cases FLOAT,
    new_deaths FLOAT,
    total_deaths FLOAT
);

CREATE TABLE covid_vaccinations (
    iso_code VARCHAR(10),
    continent VARCHAR(100),
    location VARCHAR(100),
    date DATE,
    new_vaccinations FLOAT,
    total_vaccinations FLOAT
);
