import plotly.express as px
import pandas as pd
import json
from dash import Dash, dcc, html, Input, Output
import pycountry
import unicodedata

FR_TO_EN = {
    "Afghanistan": "Afghanistan",
    "Afrique du Sud": "South Africa",
    "Albanie": "Albania",
    "Algerie": "Algeria",
    "Allemagne": "Germany",
    "Andorre": "Andorra",
    "Angola": "Angola",
    "Antigua et Barbuda": "Antigua and Barbuda",
    "Arabie Saoudite": "Saudi Arabia",
    "Argentine": "Argentina",
    "Armenie": "Armenia",
    "Australie": "Australia",
    "Autriche": "Austria",
    "Azerbaidjan": "Azerbaijan",

    "Bahamas": "Bahamas",
    "Bahrein": "Bahrain",
    "Bangladesh": "Bangladesh",
    "Barbade": "Barbados",
    "Belarus": "Belarus",
    "Bielorussie": "Belarus",
    "Belgique": "Belgium",
    "Belize": "Belize",
    "Benin": "Benin",
    "Bhoutan": "Bhutan",
    "Bolivie": "Bolivia",
    "Bosnie-Herzegovine": "Bosnia and Herzegovina",
    "Botswana": "Botswana",
    "Bresil": "Brazil",
    "Brunei": "Brunei",
    "Bulgarie": "Bulgaria",
    "Burkina Faso": "Burkina Faso",
    "Burundi": "Burundi",

    "Cambodge": "Cambodia",
    "Cameroun": "Cameroon",
    "Canada": "Canada",
    "Cap-Vert": "Cabo Verde",
    "Centrafrique": "Central African Republic",
    "Republique Centrafricaine": "Central African Republic",
    "Chili": "Chile",
    "Chine": "China",
    "Chypre": "Cyprus",
    "Colombie": "Colombia",
    "Comores": "Comoros",
    "Congo": "Republic of the Congo",
    "Republique du Congo": "Republic of the Congo",
    "RDC": "Democratic Republic of the Congo",
    "Republique Democratique du Congo": "Democratic Republic of the Congo",
    "Costa Rica": "Costa Rica",
    "Cote d'Ivoire": "Ivory Coast",
    "Croatie": "Croatia",
    "Cuba": "Cuba",

    "Danemark": "Denmark",
    "Djibouti": "Djibouti",
    "Dominique": "Dominica",

    "Egypte": "Egypt",
    "Emirats Arabes Unis": "United Arab Emirates",
    "Equateur": "Ecuador",
    "Erythree": "Eritrea",
    "Espagne": "Spain",
    "Estonie": "Estonia",
    "Eswatini": "Eswatini",
    "Ethiopie": "Ethiopia",

    "Fidji": "Fiji",
    "Finlande": "Finland",
    "France": "France",

    "Gabon": "Gabon",
    "Gambie": "Gambia",
    "Georgie": "Georgia",
    "Ghana": "Ghana",
    "Grece": "Greece",
    "Grenade": "Grenada",
    "Guatemala": "Guatemala",
    "Guinee": "Guinea",
    "Guinee Equatoriale": "Equatorial Guinea",
    "Guinee-Bissau": "Guinea-Bissau",
    "Guyana": "Guyana",

    "Haiti": "Haiti",
    "Honduras": "Honduras",
    "Hongrie": "Hungary",

    "Inde": "India",
    "Indonesie": "Indonesia",
    "Irak": "Iraq",
    "Iran": "Iran",
    "Irlande": "Ireland",
    "Islande": "Iceland",
    "Israel": "Israel",
    "Italie": "Italy",

    "Jamaique": "Jamaica",
    "Japon": "Japan",
    "Jordanie": "Jordan",

    "Kazakhstan": "Kazakhstan",
    "Kenya": "Kenya",
    "Kirghizistan": "Kyrgyzstan",
    "Kiribati": "Kiribati",
    "Koweit": "Kuwait",

    "Laos": "Laos",
    "Lesotho": "Lesotho",
    "Lettonie": "Latvia",
    "Liban": "Lebanon",
    "Liberia": "Liberia",
    "Libye": "Libya",
    "Liechtenstein": "Liechtenstein",
    "Lituanie": "Lithuania",
    "Luxembourg": "Luxembourg",

    "Macedoine du Nord": "North Macedonia",
    "Madagascar": "Madagascar",
    "Malaisie": "Malaysia",
    "Malawi": "Malawi",
    "Maldives": "Maldives",
    "Mali": "Mali",
    "Malte": "Malta",
    "Maroc": "Morocco",
    "Marshall": "Marshall Islands",
    "Maurice": "Mauritius",
    "Mauritanie": "Mauritania",
    "Mexique": "Mexico",
    "Micronesie": "Micronesia",
    "Moldavie": "Moldova",
    "Monaco": "Monaco",
    "Mongolie": "Mongolia",
    "Montenegro": "Montenegro",
    "Mozambique": "Mozambique",
    "Myanmar": "Myanmar",

    "Namibie": "Namibia",
    "Nauru": "Nauru",
    "Nepal": "Nepal",
    "Nicaragua": "Nicaragua",
    "Niger": "Niger",
    "Nigeria": "Nigeria",
    "Norvege": "Norway",
    "Nouvelle-Zelande": "New Zealand",

    "Oman": "Oman",
    "Ouganda": "Uganda",
    "Ouzbekistan": "Uzbekistan",

    "Pakistan": "Pakistan",
    "Palaos": "Palau",
    "Palestine": "Palestine",
    "Panama": "Panama",
    "Papouasie-Nouvelle-Guinee": "Papua New Guinea",
    "Paraguay": "Paraguay",
    "Pays-Bas": "Netherlands",
    "Perou": "Peru",
    "Philippines": "Philippines",
    "Pologne": "Poland",
    "Portugal": "Portugal",

    "Qatar": "Qatar",

    "Roumanie": "Romania",
    "Royaume-Uni": "United Kingdom",
    "Russie": "Russian Federation",
    "Rwanda": "Rwanda",

    "Saint-Kitts-et-Nevis": "Saint Kitts and Nevis",
    "Saint-Marin": "San Marino",
    "Saint-Vincent-et-les-Grenadines": "Saint Vincent and the Grenadines",
    "Sainte-Lucie": "Saint Lucia",
    "Salomon": "Solomon Islands",
    "Salvador": "El Salvador",
    "Samoa": "Samoa",
    "Sao Tome-et-Principe": "Sao Tome and Principe",
    "Senegal": "Senegal",
    "Serbie": "Serbia",
    "Seychelles": "Seychelles",
    "Sierra Leone": "Sierra Leone",
    "Singapour": "Singapore",
    "Slovaquie": "Slovakia",
    "Slovenie": "Slovenia",
    "Somalie": "Somalia",
    "Soudan": "Sudan",
    "Soudan du Sud": "South Sudan",
    "Sri Lanka": "Sri Lanka",
    "Suede": "Sweden",
    "Suisse": "Switzerland",
    "Suriname": "Suriname",
    "Syrie": "Syria",

    "Tadjikistan": "Tajikistan",
    "Tanzanie": "Tanzania",
    "Tchad": "Chad",
    "Tchequie": "Czechia",
    "Thailande": "Thailand",
    "Timor oriental": "Timor-Leste",
    "Togo": "Togo",
    "Tonga": "Tonga",
    "Trinite-et-Tobago": "Trinidad and Tobago",
    "Tunisie": "Tunisia",
    "Turkmenistan": "Turkmenistan",
    "Turquie": "Turkey",
    "Tuvalu": "Tuvalu",

    "Ukraine": "Ukraine",
    "Uruguay": "Uruguay",
    "USA": "United States",
    "Etats-Unis": "United States",

    "Vanuatu": "Vanuatu",
    "Vatican": "Vatican City",
    "Venezuela": "Venezuela",
    "Vietnam": "Vietnam",

    "Yemen": "Yemen",

    "Zambie": "Zambia",
    "Zimbabwe": "Zimbabwe",
}

# 1) Normalisation : accents, apostrophes, espaces, minuscule

def normalize(s: str) -> str:
    if not isinstance(s, str):
        return ""
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')  # enlever accents
    s = s.replace("’", "'")  # apostrophe typographique → apostrophe normale
    s = s.replace("-", " ")  # tiret → espace
    s= s.replace(" ", "")  # enlever espaces
    return s.strip()

def country_en(name):
    norm_name = normalize(name)
    for fr, en in FR_TO_EN.items():
        if normalize(fr) == norm_name or normalize(en) == norm_name:
            return en
    return None

# 3) Conversion vers ISO-3 (FRA, USA…)

def to_iso3(name: str) -> str | None:
    eng = country_en(name)
    if eng is None:
        return None

    try:
        return pycountry.countries.lookup(eng).alpha_3
    except LookupError:
        return None

class HeatMap:
    def __init__(self, data):
        self.data = data
        self.loc_data = data['metadata']['all']['loc']
        self.df = self._prepare_data()

    def _prepare_data(self):
        countries = list(self.loc_data.keys())
        valid, invalid, converted = self._check_country_list(countries, self.loc_data)
        
        df = pd.DataFrame(converted)
        return df

    def _check_country_list(self, country_list, dic):
        valid = []
        invalid = []
        converted = []

        for raw in country_list:
            english = country_en(raw)
            iso3 = to_iso3(raw)

            if english is None or iso3 is None:
                invalid.append(raw)
            else:
                valid.append(raw)
                converted.append({
                    "input": raw, 
                    "english": english, 
                    "iso3": iso3,
                    "count": dic.get(raw, 0)
                })

        return valid, invalid, converted

    def get_layout(self):
        fig = px.choropleth(
            self.df,
            locations="iso3",
            color="count",
            hover_name="english",
            color_continuous_scale=px.colors.sequential.Plasma,
            projection="natural earth",
            title="Répartition mondiale des occurrences"
        )
        
        return html.Div([
            dcc.Graph(figure=fig)
        ])

    def get_callbacks(self, app):
        pass
