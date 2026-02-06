"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

### 1. Importation des librairies et chargement des données
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Chargement des données
#df = pd.read_csv("........ds_salaries.csv")
# Chargement des données
df = pd.read_csv("projet/data/ds_salaries.csv")




### 2. Exploration visuelle des données
#votre code 
st.title("📊 Visualisation des Salaires en Data Science")
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")


if st.checkbox("Afficher un aperçu des données"):
    #st.write(df.....)
    st.markdown("Premières lignes du jeu de données")
    st.write(df.head(5)) # Affiche les 5 premières lignes
    


#Statistique générales avec describe pandas 
#votre code 
st.subheader("📌 Statistiques générales")
st.write(df.describe()) #Decrit les focntion numerique avec moyenne quartiles max  min
st.markdown("""
**Interprétation :** Ici 4 vairbles deux qualitatives discrets et deux quantitative continue \n
    Discrete = \n
        work_year (L'années de travail)\n
        remote_ratio (Statue teletravail)\n
    Continue = \n
        salary (salaire)\n
        salary_in_usd (salaire en usd)\n
""")

### 3. Distribution des salaires en France par rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
#votre code 
st.subheader("📈 Distribution des salaires en France")
df_fr = df[df['company_location'] == 'FR'] #trier le jeu de donnees pour ne garder que les données ou company location et france
boxplot_bar = px.box(
    df_fr,
    x='experience_level',
    y='salary_in_usd',
    title="Salaire moyen en france par niveau d'experience",
    labels={"experience_level":"Niveau Experience", "salary_in_usd": "Salaire Moyen (USD)"},
    color='experience_level'
) # Creation du graphique box plot 
st.plotly_chart(boxplot_bar)    
    
st.markdown("""
**Interprétation :** 
Distribution des salaires correles avec le niveaux d'experience en france
""")




### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 
st.subheader("📈 Salaire moyen par catégorie")
categories = ['experience_level', 'employment_type', 'job_title', 'company_location']
choix_utilisateur = st.selectbox("Quelle catégorie souhaitez-vous analyser ?", categories)
df_moyenne_choix = df.groupby(choix_utilisateur)['salary_in_usd'].mean().reset_index()
df_moyenne_choix = df_moyenne_choix.sort_values(by='salary_in_usd', ascending=False)

fig_bar = px.bar(
    df_moyenne_choix,
    x=choix_utilisateur,
    y='salary_in_usd',
    title=f"Salaire moyen par {choix_utilisateur}",
    labels={choix_utilisateur: "Catégorie", "salary_in_usd": "Salaire Moyen (USD)"},
    color='salary_in_usd',
    color_continuous_scale='Viridis'
)

st.plotly_chart(fig_bar)

st.subheader("🔗 Corrélations entre variables numériques")
### 5. Corrélation entre variables
# Sélectionner uniquement les colonnes numériques pour la corrélation
#votre code 
df_numeric = df.select_dtypes(include=[np.number])



# Calcul de la matrice de corrélation
#votre code
st.subheader("matrice de corrélation")
correlations_Pearson=df_numeric.corr() 
st.write(correlations_Pearson)

st.markdown("""
**Interprétation :** 
Ici aucune correlation est assez importante pour etre etudier essayons avec deux autre variables
""")
# Affichage du heatmap avec sns.heatmap
#votre code 
fig, ax = plt.subplots()
sns.heatmap(correlations_Pearson,annot=True, cmap='coolwarm', ax=ax) # annot=True permet d'annoter chaques carre ma heat map
st.pyplot(fig)

st.subheader (" Matrice de corrélation Salaire/Remote ")
corrélations_salaire_remote=df[["salary_in_usd","remote_ratio"]]
correlations_Pearson_salaire_remote=corrélations_salaire_remote.corr() 
st.write(correlations_Pearson_salaire_remote)
fig, ax = plt.subplots()
sns.heatmap(correlations_Pearson_salaire_remote,annot=True, cmap='coolwarm', ax=ax) # annot=True permet d'annoter chaques carre ma heat map
st.pyplot(fig)

st.markdown("""
**Interprétation :** 
Ici aucune correlation entre la variable salaire et celui du teletravil essayons de voir si le salaire depend de l'experience
""")


st.subheader(" Matrice de corrélation Salaire/Expérience")

df_corr = df.copy()
mapping_xp = {"EN": 1, "MI": 2, "SE": 3, "EX": 4}
df_corr['experience_level_num'] = df_corr['experience_level'].map(mapping_xp)

colonnes_cibles = ["salary_in_usd", "experience_level_num"]
correlations_Pearson = df_corr[colonnes_cibles].corr()

st.write(correlations_Pearson)

fig, ax = plt.subplots()
sns.heatmap(correlations_Pearson, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.markdown("""
**Interprétation :** 
Ici il y a une correlation moyenne de 0.44 soit 44% entre l'experience d'un employer et son salaire donc le salaire a tendance à augmenter avec l'expérience. \n

Cependant, l'expérience n'est pas le seul facteur, car elle n'explique qu'une partie de la variabilité totale des revenus. \n

Le pouvoir explicatif ($R^2$) : Pour savoir à quel point l'expérience "explique" la variance du salaire, on doit élever $r$ au carré : 0.44*0.44 = 0.19 \n

Cela signifie que l'expérience explique environ 19% de la variation des salaires. Les 81% restants dépendent d'autres facteurs (le pays, la taille de l'entreprise, le titre du poste


""")


### 6. Analyse interactive des variations de salaire
# Une évolution des salaires pour les 10 postes les plus courants
# count of job titles pour selectionner les postes
# calcule du salaire moyen par an
#utilisez px.line
#votre code 

top10_names = df['job_title'].value_counts().head(10).index # On utilise value_counts() pour compter l'occurrence de chaque métier

df_top10 = df[df['job_title'].isin(top10_names)]

salaire_moyen_evolution = df_top10.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().reset_index()

graph_evolution_line = px.line(
    salaire_moyen_evolution,
    x='work_year',
    y='salary_in_usd',
    color='job_title', # C'est ici qu'on crée une ligne par métier !
    title="Évolution du salaire moyen par poste (Top 10)"
)

st.plotly_chart(graph_evolution_line)

graph_evolution_bar = px.bar(
    salaire_moyen_evolution,
    x='work_year',
    y='salary_in_usd',
    color='job_title', # C'est ici qu'on crée une ligne par métier !
    title="Évolution du salaire moyen par poste (Top 10)"
)

st.plotly_chart(graph_evolution_bar)
st.markdown("""
**Interprétation :** 
Ici on voit une augmentation du nombre de metier dans la data soit un croissance dans ce domaines
""")

#salaire_moyen_top10_job = top10_job.groupby('work_year')['salary_in_usd'].mean().sort_values(ascending=False)
#graph_salaire_moyen_annes = px.line(
    #salaire_moyen_top10_job,
    #x='work_year',
    #y='salary_in_usd'
#)
#st.plotly_chart(graph_salaire_moyen_annes)

 



### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar
#votre code 

st.subheader(" Salaire médian par expérience et taille d'entreprise")
df_median = df.groupby(['experience_level', 'company_size'])['salary_in_usd'].median().reset_index()
fig_median = px.bar(
    df_median,
    x='experience_level',
    y='salary_in_usd',
    color='company_size',
    barmode='group', 
    title="Salaire médian par niveau d'expérience et taille d'entreprise",
    category_orders={
        "experience_level": ["EN", "MI", "SE", "EX"],
        "company_size": ["S", "M", "L"]
    },
    color_discrete_sequence=px.colors.qualitative.Pastel
)

st.plotly_chart(fig_median)




### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages 
#votre code 

st.subheader("Filtrer par tranche de salaire")
min_sal = int(df['salary_in_usd'].min())
max_sal = int(df['salary_in_usd'].max())
intervalle_salaire = st.slider(
    "Sélectionnez une plage de salaires (USD)",
    min_value=min_sal,
    max_value=max_sal,
    value=(min_sal, max_sal) # Valeur par défaut : toute la plage
)




### 9.  Impact du télétravail sur le salaire selon le pays

top_pays = df['company_location'].value_counts().head(10).index
df_top10_pays = df[df['company_location'].isin(top_pays)]
df_impact = df_top10_pays.groupby(['company_location', 'remote_ratio'])['salary_in_usd'].mean().reset_index()

fig_impact = px.bar(
    df_impact,
    x='company_location', # On utilise la localisation ici
    y='salary_in_usd',
    color='remote_ratio',
    barmode='group',
    title="Impact du télétravail sur le salaire selon le pays"
)

st.plotly_chart(fig_impact)

### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 


st.subheader(" Filtrage croisé expérience et taille d'entreprise")
options_xp = df['experience_level'].unique()
options_taille = df['company_size'].unique()
choix_xp = st.multiselect("Sélectionnez le niveau d'expérience", options_xp, default=options_xp)
choix_taille = st.multiselect("Sélectionnez la taille d'entreprise", options_taille, default=options_taille)
