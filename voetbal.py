import pandas as pd
import statsmodels.api as sm
import numpy as np
import streamlit as st
import seaborn as sns



FIFA15 = pd.read_csv('players_15.csv', low_memory=False)
FIFA15 = FIFA15[['sofifa_id', 'short_name', 'long_name', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob',
                 'height_cm', 'weight_kg', 'club_name', 'league_name', 'club_position', 'nationality', 'preferred_foot', 
                 'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]
FIFA16 = pd.read_csv('players_16.csv', low_memory=False)
FIFA16 = FIFA16[['sofifa_id', 'short_name', 'long_name', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob',
                 'height_cm', 'weight_kg', 'club_name', 'league_name', 'club_position', 'nationality', 'preferred_foot', 
                 'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]
FIFA17 = pd.read_csv('players_17.csv', low_memory=False)
FIFA17 = FIFA17[['sofifa_id', 'short_name', 'long_name', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob',
                 'height_cm', 'weight_kg', 'club_name', 'league_name', 'club_position', 'nationality', 'preferred_foot', 
                 'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]
FIFA18 = pd.read_csv('players_18.csv', low_memory=False)
FIFA18 = FIFA18[['sofifa_id', 'short_name', 'long_name', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob',
                 'height_cm', 'weight_kg', 'club_name', 'league_name', 'club_position', 'nationality', 'preferred_foot', 
                 'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]
FIFA19 = pd.read_csv('players_19.csv', low_memory=False)
FIFA19 = FIFA19[['sofifa_id', 'short_name', 'long_name', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob',
                 'height_cm', 'weight_kg', 'club_name', 'league_name', 'club_position', 'nationality', 'preferred_foot', 
                 'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]
FIFA20 = pd.read_csv('players_20.csv', low_memory=False)
FIFA20 = FIFA20[['sofifa_id', 'short_name', 'long_name', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob',
                 'height_cm', 'weight_kg', 'club_name', 'league_name', 'club_position', 'nationality', 'preferred_foot', 
                 'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]
FIFA21 = pd.read_csv('players_21.csv', low_memory=False)
FIFA21 = FIFA21[['sofifa_id', 'short_name', 'long_name', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob',
                 'height_cm', 'weight_kg', 'club_name', 'league_name', 'club_position', 'nationality', 'preferred_foot', 
                 'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]
FIFA22 = pd.read_csv('players_22.csv', low_memory=False)
FIFA22 = FIFA22[['sofifa_id', 'short_name', 'long_name', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob',
                 'height_cm', 'weight_kg', 'club_name', 'league_name', 'club_position', 'nationality', 'preferred_foot', 
                 'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]


FIFA15['club_name'] = FIFA15['club_name'].fillna('No club')
FIFA15['league_name'] = FIFA15['league_name'].fillna('No league')
FIFA15['club_position'] = FIFA15['club_position'].fillna('No position')
FIFA16['club_name'] = FIFA16['club_name'].fillna('No club')
FIFA16['league_name'] = FIFA16['league_name'].fillna('No league')
FIFA16['club_position'] = FIFA16['club_position'].fillna('No position')
FIFA17['club_name'] = FIFA17['club_name'].fillna('No club')
FIFA17['league_name'] = FIFA17['league_name'].fillna('No league')
FIFA17['club_position'] = FIFA17['club_position'].fillna('No position')
FIFA18['club_name'] = FIFA18['club_name'].fillna('No club')
FIFA18['league_name'] = FIFA18['league_name'].fillna('No league')
FIFA18['club_position'] = FIFA18['club_position'].fillna('No position')
FIFA19['club_name'] = FIFA19['club_name'].fillna('No club')
FIFA19['league_name'] = FIFA19['league_name'].fillna('No league')
FIFA19['club_position'] = FIFA19['club_position'].fillna('No position')
FIFA20['club_name'] = FIFA20['club_name'].fillna('No club')
FIFA20['league_name'] = FIFA20['league_name'].fillna('No league')
FIFA20['club_position'] = FIFA20['club_position'].fillna('No position')
FIFA21['club_name'] = FIFA21['club_name'].fillna('No club')
FIFA21['league_name'] = FIFA21['league_name'].fillna('No league')
FIFA21['club_position'] = FIFA21['club_position'].fillna('No position')
FIFA22['club_name'] = FIFA22['club_name'].fillna('No club')
FIFA22['league_name'] = FIFA22['league_name'].fillna('No league')
FIFA22['club_position'] = FIFA22['club_position'].fillna('No position')

fig = sns.regplot(x="overall",y="value_eur",data=FIFA15,ci=None)
st.plotly_chart(fig)
