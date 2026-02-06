# Projet Jupyter Notebook

## Description du Projet & Données

Ce projet analyse les salaires dans le domaine de la Data Science à travers le monde. L'application interactive permet d'explorer les rémunérations en fonction de l'expérience, du type de poste, de la localisation géographique (avec un focus sur la France) et de l'impact du télétravail.

### Les Données
Le jeu de données utilisé contient les colonnes suivantes :
* **work_year** : L'année de versement du salaire.
* **experience_level** : Le niveau d'expérience (EN: Débutant, MI: Intermédiaire, SE: Senior, EX: Expert).
* **job_title** : L'intitulé du poste (Data Scientist, ML Engineer, etc.).
* **salary_in_usd** : Le salaire converti en dollars US (pour faciliter la comparaison).
* **remote_ratio** : Le pourcentage de travail effectué à distance.
* **company_location** : Le pays du siège social de l'entreprise.
* **company_size** : La taille de l'entreprise (S, M, L).

---

##  Références des données

Les données utilisées pour cette analyse proviennent de la plateforme **Kaggle**. 

* **Source principale** : [Data Science Salaries 2024 (ou l'année correspondante)](https://www.kaggle.com/)
* **Auteur du dataset** : (Optionnel : Ajoute le nom de l'auteur si tu le trouves sur la page Kaggle, ex: *Hummaam Zahid*)
* **Licence** : CC0: Public Domain (Généralement le cas pour ces datasets, à vérifier sur la page).
* **Accès direct** : Vous pouvez retrouver le fichier original sous le nom `ds_salaries.csv`.


## Installation et Lancement

1. Clonez le dépôt :
   `git clone [URL_DE_TON_DEPOT]`
2. Installez les dépendances :
   `pip install -r requirements.txt`
3. Lancez l'application :
   `streamlit run application.py`




## Lien application Streamlit & Github
   
lien github = https://github.com/MaxenceLR/projet_notebook

lien application streamlit = https://projetnotebook-aeyhk4n6nk2jjybcnoxn58.streamlit.app/