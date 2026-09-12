import streamlit as st

dashboard = st.Page('Dashboard.py',title='📈Dashboard')
form = st.Page('form.py',title='📄Form')
eda_report = st.Page('EDA.py',title='📊EDA Report')
models = st.Page('models.py',title='⚙️Models')
analysis = st.Page('data_visualization.py',title='🔍Data Analysis')
pg = st.navigation({
    '🏠Home':[dashboard,eda_report,models,analysis],
    'Prediction Form':[form]
})

pg.run()