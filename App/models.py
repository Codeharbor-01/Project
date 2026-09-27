import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader('**🔭 Model Overview**',anchor='model_overview')

st.markdown("""
    <div class='box'>
        <p>This system uses machine learning regression models <strong>to predict a students' final examination score based on their academic and personal characteristics.</strong></p>
        <p>The below mentioned models are used in the making of this project.</p>
        <ol>
            <li>KNN Regression</li>
            <li>Linear Regression</li>
            <li>Random Forest Regression</li>
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

st.subheader('**ℹ️ Model Description**')
st.markdown("""
    <br>
    <div class='flexes'>
        <div class='flex1'>
            <div class='flex_col1'>
                <p class='icon'>👥</p>       
            </div>
            <div class='flex_col1'>
                <p class='title'>KNN Model</p>
                <p class='desc'>
                    KNN Regression is a supervised machine learning algorithm that predicts a continuous value by examining the closest data points in the dataset. It makes predictions based on the average values of its nearest neighbours, making it useful for finding patterns between similar student records.
                </p>
            </div>
        </div>
        <div class='flex2'> 
            <div class='flex_col1'> 
                <p class='icon'>📈</p>        
            </div> 
            <div class='flex_col1'> 
                <p class='title'>Linear Regression</p> 
                <p class='desc'> 
                    Linear Regression is a supervised machine learning algorithm that predicts a continuous value by identifying the relationship between input features and the target variable. It estimates the final CGPA by fitting a linear relationship between factors such as attendance, study hours, previous CGPA, and other student characteristics. 
                </p> 
            </div> 
        </div>
        <div class='flex3'> 
            <div class='flex_col1'> 
                <p class='icon'>⚡</p>        
            </div> 
            <div class='flex_col1'> 
                <p class='title'>SVR Model</p> 
                <p class='desc'> 
                    Support Vector Regression (SVR) is a supervised machine learning algorithm that predicts continuous values by finding a function that fits the data within an acceptable margin of error. It can capture complex relationships between student characteristics and final CGPA, making it useful for predicting academic performance. 
                </p> 
            </div> 
        </div>
        <div class='flex4'> 
            <div class='flex_col1'> 
                <p class='icon'>🌲</p>        
            </div> 
            <div class='flex_col1'> 
                <p class='title'>Random Forest Model</p> 
                <p class='desc'> 
                    Random Forest Regression is a supervised machine learning algorithm that combines multiple decision trees to make predictions. Each tree produces a prediction and the results are combined to estimate the final CGPA. By using multiple trees, Random Forest can capture complex relationships within student performance data and provide accurate predictions. 
                </p> 
            </div> 
        </div>
    </div>

    <style>
        .flexes .flex1, .flex2, .flex3, .flex4{
            display:flex;
            border:1px solid lightgray;
            margin-bottom:10px;
            padding:20px 20px;
            border-radius:10px;
            box-shadow:0 2px 8px rgba(0,0,0,0.4);
            transition:0.2s
        }

        .flex_col1 .icon{
            font-size:100px;
            width:150px;
        }

        .flexes .title{
            font-size:20px;
            font-weight: 300px;
        }

        .flexes .flex1:hover, .flex2:hover, .flex3:hover, .flex4:hover{
            transform: translateY(-3px);
            box-shadow:0 4px 10px rgba(0,0,0,0.6)
        }
    </style>
""",unsafe_allow_html=True)
st.divider()

st.subheader('**📖 Understanding the Metrics**')

st.markdown("""
<table style="width:100%; border-collapse:collapse;">
    <tr>
        <th style="padding:12px; text-align:left; border-bottom:1px solid #ccc;">
            Metric
        </th>
        <th style="padding:12px; text-align:left; border-bottom:1px solid #ccc;">
            What it tells us
        </th>
        <th style="padding:12px; text-align:left; border-bottom:1px solid #ccc;">
            Better value
        </th>
    </tr>
    <tr>
        <td style="padding:12px; border-bottom:1px solid #ddd;">
            <strong>R² Score</strong>
        </td>
        <td style="padding:12px; border-bottom:1px solid #ddd;">
            How well the model explains variation in CGPA
        </td>
        <td style="padding:12px; border-bottom:1px solid #ddd;">
            <strong>Higher</strong>
        </td>
    </tr>
    <tr>
        <td style="padding:12px; border-bottom:1px solid #ddd;">
            <strong>MAE</strong>
        </td>
        <td style="padding:12px; border-bottom:1px solid #ddd;">
            Average difference between predicted and actual CGPA
        </td>
        <td style="padding:12px; border-bottom:1px solid #ddd;">
            <strong>Lower</strong>
        </td>
    </tr>
    <tr>
        <td style="padding:12px;">
            <strong>RMSE</strong>
        </td>
        <td style="padding:12px;">
            Prediction error, with larger errors weighted more heavily
        </td>
        <td style="padding:12px;">
            <strong>Lower</strong>
        </td>
    </tr>
</table>
<br>
""", unsafe_allow_html=True)

st.write("""
**Why use these metrics?**<br>
R² evaluates how well the model explains the data, while MAE and RMSE
measure prediction error. Together, they provide a broader view of model performance.
""",unsafe_allow_html=True)

st.divider()

linear_scores = joblib.load(r'Scores/Linear_Score.pkl')
KNN_scores = joblib.load(r'Scores/KNN_Score.pkl')
SVR_scores = joblib.load(r'Scores/SVR_Scores.pkl')
RandomForest_scores = joblib.load(r'Scores\RandomForest_Scores.pkl')

scores_dict = {
    'Models':[
        'KNN',
        'Linear',
        'RandomForest',
        'SVR'
    ],

    'R2':[
        round(KNN_scores['r2'],2),
        round(linear_scores['r2'],2),
        round(RandomForest_scores['r2'],2),
        round(SVR_scores['r2'],2)
    ],

    'Mean Absolute Error':[
        round(KNN_scores['mae'],2),
        round(linear_scores['mae'],2),
        round(RandomForest_scores['mae'],2),
        round(SVR_scores['mae'],2)
    ],

    'Root Mean Squared Error':[
        round(KNN_scores['rmse'],2),
        round(linear_scores['rmse'],2),
        round(RandomForest_scores['rmse'],2),
        round(SVR_scores['rmse'],2)
    ],
}

st.subheader('**🏆 Leaderboards**')
st.markdown(f"""
    <div class='leaderboard_table'>
        <table>
            <tr id='header'>
                <th>Rank</th>
                <th>Model</th>
                <th>R<sup>2</sup> Score</th>
            </tr>
            <tr id='first'>
                <td>🥇</td>
                <td>RandomForest Regression</td>
                <td>{scores_dict['R2'][2]}</td>
            </tr>
            <tr id='second'>
                <td>🥈</td>
                <td>SVR Regression</td>
                <td>{scores_dict['R2'][3]}</td>
            </tr>
            <tr id='third'>
                <td>🥉</td>
                <td>Linear Regression</td>
                <td>{scores_dict['R2'][1]}</td>
            </tr>
        </table>
    </div>
    <style>
        .leaderboard_table table{{
            width:100%;
        }}

        .leaderboard_table #header{{
            background-color:rgba(0,0,0,0.19);
        }}

        .leaderboard_table #first{{
            background-color:rgba(255,215,0,0.9)
        }}

        .leaderboard_table #second{{
            background-color:rgba(229,228,226,0.9)
        }}

        .leaderboard_table #third{{
            background-color:rgba(207,127,50,0.5)
        }}
    </style>
""",unsafe_allow_html=True)

st.divider()

st.subheader('📊 Model Scores')

st.markdown(f"""
    <table class='scores_table'>
        <tr>
            <th>Model</th>
            <th>R<sup>2</sup> Score</th>
            <th>Mean Absolute Error</th>
            <th>Root Mean Square Error</th>
        </tr>
        <tr>
            <td>KNN</td>
            <td>{scores_dict['R2'][0]}</td>
            <td>{scores_dict['Mean Absolute Error'][0]}</td>
            <td>{scores_dict['Root Mean Squared Error'][0]}</td>
        </tr>
        <tr>
            <td>Linear</td>
            <td>{scores_dict['R2'][1]}</td>
            <td>{scores_dict['Mean Absolute Error'][1]}</td>
            <td>{scores_dict['Root Mean Squared Error'][1]}</td>
        </tr>
        <tr>
            <td>RandomForest</td>
            <td>{scores_dict['R2'][2]}</td>
            <td>{scores_dict['Mean Absolute Error'][2]}</td>
            <td>{scores_dict['Root Mean Squared Error'][2]}</td>
        </tr>
        <tr>
            <td>SVR</td>
            <td>{scores_dict['R2'][3]}</td>
            <td>{scores_dict['Mean Absolute Error'][3]}</td>
            <td>{scores_dict['Root Mean Squared Error'][3]}</td>
        </tr>
    </table>

    <style>
        .scores_table{{
            width:100%;
        }}

        .scores_table tr:nth-child(odd){{
            background-color:rgba(0,0,0,0.1)
        }}

    </style>
""",unsafe_allow_html=True)

st.divider()

st.subheader('**🔍 Model Score Comparison**',anchor='comparison')
score_comp = st.container(border=True)
scores_df = pd.DataFrame(scores_dict)

score_comp.markdown("""
    <p id='r2'>1. 🎯 R<sup>2</sup> Score</p>

    <style>
        #r2{
            font-size:20px;
            margin-top:10px;
        }
    </style>

""",unsafe_allow_html=True)

fig,ax = plt.subplots()
sns.barplot(scores_df.sort_values(ascending=False,by='R2'),x='Models',y='R2',ax=ax,hue='Models')
ax.set_xlabel('Models')
ax.set_ylabel('R2 Score')
plt.tight_layout()

for container in ax.containers:
    ax.bar_label(container)
score_comp.pyplot(fig)

score_comp.divider()

score_comp.markdown("""
    <p id='mae'>2. 📏 Mean Absolute Error Score</p>

    <style>
        #mae{
            font-size:20px;
        }
    </style>

""",unsafe_allow_html=True)

fig,ax = plt.subplots()
sns.barplot(scores_df.sort_values(ascending=True,by='Mean Absolute Error'),x='Models',y='Mean Absolute Error',ax=ax,hue='Models')
ax.set_xlabel('Models')
ax.set_ylabel('Mean Absolute Error Score')
plt.tight_layout()

for container in ax.containers:
    ax.bar_label(container)
score_comp.pyplot(fig)

score_comp.divider()

score_comp.markdown("""
    <p id='rmse'>3. 📐 Root Mean Squared Error</p>

    <style>
        #rmse{
            font-size:20px;
        }
    </style>

""",unsafe_allow_html=True)

fig,ax = plt.subplots()
sns.barplot(scores_df.sort_values(ascending=True,by='Root Mean Squared Error'),x='Models',y='Root Mean Squared Error',ax=ax,hue='Models')
ax.set_xlabel('Models')
ax.set_ylabel('Root Mean Squared Error')
plt.tight_layout()

for container in ax.containers:
    ax.bar_label(container)
score_comp.pyplot(fig)
