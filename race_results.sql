-- Qusestion 1: Write a query that will display race results from 2020 and ordered by driver points

SELECT
    circuit_location,
    grid, 
    driver_number,
    fastest_lap,
    points,
    driver_name,
    race_name,
    race_time,
    race_year,
    team,
    CURRENT_TIMESTAMP AS created_at
FROM
    races
    JOIN circuits ON races.circuit_location = circuits.circuit_location
    JOIN drivers ON races.driver_name = drivers.driver_name
    JOIN constructors ON races.team = constructors.team
    JOIN results ON races.race_time = results.race_time
WHERE
    race_year = 2020
ORDER BY
    points DESC