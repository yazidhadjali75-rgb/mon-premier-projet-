CREATE OR REPLACE TABLE `mon-projet-bigquery-511118.fr_carburant.data_prep_fr_carburant` AS
SELECT
  id,
  adresse,
  ville,
  code_postal,
  CONCAT(adresse, ', ', code_postal, ' ', ville) AS adresse_complete,
  latitude,
  longitude,
  CONCAT(latitude, ',', longitude) AS coordonnees,
  prix_sp95,
  ROUND(ST_DISTANCE(
    ST_GEOGPOINT(longitude, latitude),
    ST_GEOGPOINT(2.3417, 48.9565)
  ) / 1000, 1) AS distance_km
FROM `mon-projet-bigquery-511118.fr_carburant.fr_carburant`
WHERE (code_postal BETWEEN 75000 AND 75999
   OR code_postal BETWEEN 92000 AND 94999)
  AND prix_sp95 BETWEEN 1 AND 3;
