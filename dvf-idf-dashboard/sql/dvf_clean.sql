-- Vue nettoyée des données DVF pour le dashboard Looker Studio
-- Projet BigQuery : immobilier-idf-analysis / dataset : immobilier_idf

CREATE OR REPLACE VIEW `immobilier-idf-analysis.immobilier_idf.dvf_clean` AS
SELECT
  *,
  `Code departement` AS code_departement,
  `Valeur fonciere` AS valeur_fonciere,
  `Surface reelle bati` AS surface_bati,
  `Type local` AS type_local,
  `Date mutation` AS date_mutation,
  DATE_TRUNC(`Date mutation`, MONTH) AS mois,
  SAFE_DIVIDE(`Valeur fonciere`, `Surface reelle bati`) AS prix_m2,
  CONCAT(CAST(`Code departement` AS STRING), ' - ', Commune) AS commune_dep,
  CONCAT('FR-', CAST(`Code departement` AS STRING)) AS code_region,
  EXTRACT(YEAR FROM `Date mutation`) AS annee
FROM `immobilier-idf-analysis.immobilier_idf.dvf_raw`
WHERE `Nature mutation` = 'Vente'
  AND `Type local` IN ('Appartement', 'Maison')
  AND `Code departement` IN (75, 77, 78, 91, 92, 93, 94, 95)
  AND `Valeur fonciere` > 1000
  AND `Surface reelle bati` > 9
  AND SAFE_DIVIDE(`Valeur fonciere`, `Surface reelle bati`) BETWEEN 500 AND 30000;
