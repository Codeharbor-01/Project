import streamlit as st

st.subheader('**🔭Model Overview**',anchor='model_overview')

st.markdown("""
    <div class='box'>
        <p>This system uses machine learning regression models <strong>to predict a students' final examination score based on their academic and personal characteristics.</strong></p>
        <p>The below mentioned models are used in the making of this project.</p>
        <ol>
            <li>KNN Regression</li>
            <li>Linear Regression</li>
            <li>Support Vector Regression (SVR)</li>
        </ol>
    </div>

    <style>
        .box{
            border: 1px solid rgba(0,0,0,1);
            border-radius:15px;
            padding:20px 20px;
        }
    </style>
""",unsafe_allow_html=True)

st.divider()

st.subheader('**Model Description**')
st.markdown("""
    <div class='flexes'>
        <div class='flex1'>
            <p class='icon'>👥</p>
            <p class='icon'>KNN Model</p>
            <p class='desc>
                KNN Regression is a supervised machine learning algorithm that predicts a continuous value by examining the closest data points in the dataset. It makes predictions based on the average values of its nearest neighbours, making it useful for finding patterns between similar student records.
            </p>
        </div>
    </div>
    <style>
        .flexes{
            display:flex;
        }

    </style>
""",unsafe_allow_html=True)