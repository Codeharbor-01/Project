import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r'Dataset/cleaned_student_data.csv')
modified_df = df.drop(columns='Student_ID')
st.header('**👀 Data Visualization (Dynamic)**')
st.text('This page allows users to dynamically view datasets by selecting respective columns.' \
' Users can also choose respective chart types to view the data.')

col1,col2 = st.columns(2)

X = col1.selectbox(label='X-axis',options=list(modified_df.columns))
Y = col2.selectbox(label='Y-axis',options=list(modified_df.columns))

num_cols = modified_df.select_dtypes([int,float]).columns
cat_cols = modified_df.select_dtypes(str).columns

available_options = []

if X in num_cols and Y in num_cols:
    available_options=['Scatter Plot','Line Chart']

elif (X in num_cols and Y in cat_cols) or (X in cat_cols and Y in num_cols):
    available_options = ['Bar Chart','Box Plot','Violin Plot']

elif X in cat_cols and Y in cat_cols:
    available_options = ['Bar Chart']

chart = st.selectbox(label='Chart',options=available_options)

if chart=='Bar Chart':
    fig,ax = plt.subplots()
    sns.barplot(modified_df,x=X,y=Y,ax=ax)
    plt.tight_layout()
    for container in ax.containers:
        plt.bar_label(container,fmt='%.2f',padding=-120,color='white')
    st.pyplot(fig)

elif chart=='Box Plot':
    fig,ax = plt.subplots()
    sns.boxplot(modified_df,x=X,y=Y,ax=ax)
    plt.tight_layout()
    st.pyplot(fig)

elif chart=='Scatter Plot':
    fig,ax = plt.subplots()
    sns.scatterplot(modified_df,x=X,y=Y,ax=ax)
    plt.tight_layout()
    st.pyplot(fig)

elif chart=='Line Chart':
    fig,ax = plt.subplots()
    sns.lineplot(modified_df,x=X,y=Y,ax=ax)
    plt.tight_layout()
    st.pyplot(fig)

elif chart=='Violin Plot':
    fig,ax=plt.subplots()
    sns.violinplot(modified_df,x=X,y=Y,ax=ax)
    plt.tight_layout()
    st.pyplot(fig)

st.divider()
st.markdown("""
    <a href="">Click Here!</a>
""",unsafe_allow_html=True)