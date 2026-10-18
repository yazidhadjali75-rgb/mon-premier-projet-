# Prix du SP95 en France : dashboard

Dashboard Looker Studio connecté à Google Sheets, construit à partir de données de prix des carburants nettoyées avec BigQuery.

**Dashboard en ligne :** [ouvrir dans Looker Studio]https://datastudio.google.com/reporting/665306b5-21da-4a00-818c-c983886ce6d7

## Outils

- **Source du dashboard :** Google Sheets
- **Visualisation :** Looker Studio
- **Préparation des données :** Google BigQuery (requête SQL de nettoyage, utilisée une seule fois)
- **Données d'origine :** prix des carburants en France (open data)

## Méthode

1. Import des données brutes dans BigQuery.
2. Nettoyage avec une requête SQL (`sql/nettoyage.sql`) : sélection des lignes utiles au SP95 et suppression des valeurs aberrantes.
3. Export des données nettoyées vers Google Sheets.
4. Le dashboard Looker Studio est connecté à cette feuille Google Sheets, pas à BigQuery.

## Ce que montre le dashboard

Des indicateurs clés et des graphiques sur les prix du SP95 : niveau moyen des prix, évolution dans le temps et comparaisons entre zones géographiques.

## Limites

- Le dashboard repose sur un échantillon de données nettoyées : les chiffres ne représentent pas forcément l'ensemble du marché.
- La période couverte est celle des données importées, elle peut être courte.
- Certaines zones peuvent compter peu de relevés, ce qui rend leurs prix moins fiables.
