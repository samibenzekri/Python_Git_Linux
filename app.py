import pandas as pd
import numpy as np
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime, time, timedelta
import csv
# Chargement des données CSV
file_path = "prix.csv"  # Remplacez par le chemin d'accès à votre fichier CSV
data = pd.read_csv(file_path,names=["date","prix"])
data["date"] = pd.to_datetime(data["date"])  # Remplacez "date" par le nom de la colonne date dans votre CSV
data["prix"] = data["prix"].astype(float)

mean_price = data["prix"].mean()
min_price = data["prix"].min()
max_price = data["prix"].max()
variance_price = data["prix"].var()
dernier_prix = data['prix'].iloc[-1]
rendement_journalier = (dernier_prix - data['prix'].iloc[-2]) / data['prix'].iloc[-2] * 100
today = datetime.now().date()

def prix_derniere_ligne_si_20h():
    maintenant = datetime.now()
    
    if maintenant.hour == 20:
        dernier_prix = data['prix'].iloc[-1]
        return dernier_prix
    else:
        return None


#Création de l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Euronext : Tableau de Synthèse {}".format(today.strftime('%d-%m-%Y')), style={'text-align': 'center'}),
    dcc.Graph(
        id="time_series",
        figure={
            "data": [{"x": data["date"], "y": data["prix"], "type": "line", "name": "Prix"}],
            "layout": {"title": "Série temporelle des prix"}
        }
    ),
    html.Table([
        html.Thead([
            html.Tr([html.Th("Statistique"), html.Th("Valeur")])
        ]),
        html.Tbody([
            html.Tr([html.Td("Moyenne"), html.Td(f"{mean_price:.2f}")]),
            html.Tr([html.Td("Minimum"), html.Td(f"{min_price:.2f}")]),
            html.Tr([html.Td("Maximum"), html.Td(f"{max_price:.2f}")]),
            html.Tr([html.Td("Variance"), html.Td(f"{variance_price:.2f}")]),
	    html.Tr([html.Td("Dernier prix"), html.Td(f"{dernier_prix:.2f}")]),
	    html.Tr([html.Td("Rendement journalier"), html.Td(f"{rendement_journalier:.2f}")]),
	    html.Tr([html.Td("Prix à 20h"), html.Td(f"{prix_derniere_ligne_si_20h():.2f}")])  
      	])
    ])
])

if __name__ == "__main__":
    app.run_server(host = "0.0.0.0", port = 8050, debug=True)

