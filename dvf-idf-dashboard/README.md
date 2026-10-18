# Marché immobilier en Île-de-France : dashboard DVF

Dashboard interactif d'analyse des ventes, des prix et des types de biens en Île-de-France, construit à partir des données DVF (Demandes de Valeurs Foncières).

**Dashboard en ligne :** [ouvrir dans Looker Studio]https://datastudio.google.com/reporting/a1693a73-1dac-407b-b29f-cfd071171764

## Outils

- **Données :** DVF, open data (data.gouv.fr)
- **Nettoyage :** Google BigQuery (vue SQL)
- **Source du dashboard :** Google Sheets (export de la vue nettoyée)
- **Visualisation :** Looker Studio

## Méthode

1. Import des données DVF brutes dans BigQuery (environ 203 570 lignes).
2. Nettoyage avec une requête SQL (`sql/dvf_clean.sql`) : ventes de maisons et d'appartements, 8 départements d'Île-de-France, suppression des valeurs aberrantes, calcul du prix au m².
3. Export des 424 lignes obtenues vers Google Sheets, puis connexion de Looker Studio.

## Ce que montre le dashboard

- Nombre de ventes, nombre de communes, prix moyen et prix médian au m²
- Évolution du prix médian par type de bien
- Prix médian par type de bien et par département
- Carte du prix médian par département
- Répartition des ventes par type de bien
- Top 5 des communes

## Limites

- Les données nettoyées ne contiennent que 424 lignes, de janvier à juin 2026 : il n'y a pas d'évolution sur plusieurs années.
- Paris représente environ 59 % des lignes, donc les prix globaux reflètent surtout le marché parisien.
- Certains départements et communes ont très peu de lignes : leurs prix médians sont fragiles.
- Le « nombre de ventes » compte des lignes de mutation, pas des ventes distinctes.
