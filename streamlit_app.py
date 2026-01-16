import streamlit as st

# Ton message de test
st.write('HelloMBADIA !')

# Ajoute ceci pour ta présentation, ça fera plus pro :

st.write("Ceci est ma première application interactive connectée à Snowflake.")


import streamlit as st
import pandas as pd
import plotly.express as px # Pour des graphiques plus beaux

st.set_page_config(page_title="Dashboard Amazon Prime", layout="wide")

st.title('🎬 Dashboard Amazon Prime Titles')

# Barre latérale pour le chargement
with st.sidebar:
    st.subheader('Configuration')
    uploaded_file = st.file_uploader("Charger le fichier amazon_prime_titles.csv", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # --- CALCUL DES INDICATEURS CLÉS (KPIs) ---
    total_titres = len(df)
    nb_films = len(df[df['type'] == 'Movie'])
    nb_series = len(df[df['type'] == 'TV Show'])
    annee_max = int(df['release_year'].max())

    # --- AFFICHAGE DES INDICATEURS ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Titres", total_titres)
    col2.metric("Films 🎥", nb_films)
    col3.metric("Séries 📺", nb_series)
    col4.metric("Année la plus récente", annee_max)

    st.divider()

    # --- VISUALISATION DES DONNÉES ---
    tab1, tab2, tab3 = st.tabs(["📊 Analyses", "📑 Données Brutes", "🔍 Statistiques"])

    with tab1:
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.subheader("Répartition Films vs Séries")
            fig_type = px.pie(df, names='type', hole=0.4, color_discrete_sequence=['#00A8E1', '#FF9900'])
            st.plotly_chart(fig_type, use_container_width=True)

        with col_right:
            st.subheader("Évolution des sorties (Top 15 ans)")
            # On compte les titres par année
            count_year = df['release_year'].value_counts().reset_index().head(15)
            fig_year = px.bar(count_year, x='release_year', y='count', labels={'count': 'Nombre', 'release_year': 'Année'})
            st.plotly_chart(fig_year, use_container_width=True)

    with tab2:
        st.subheader('Aperçu du DataFrame')
        st.dataframe(df, use_container_width=True)

    with tab3:
        st.subheader('Statistiques Descriptives')
        st.write(df.describe())

else:
    st.info('☝️ Veuillez charger le fichier CSV via la barre latérale pour activer le dashboard.')
    st.image("https://m.media-amazon.com/images/G/01/digital/video/web/logo/light/PrimeVideo_Logo_FullColor_RGB.png", width=200)
    st.image("https://m.media-amazon.com/images/G/01/digital/video/web/logo/light/PrimeVideo_Logo_FullColor_RGB.png", width=200)