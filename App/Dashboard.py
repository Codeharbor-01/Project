import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

st.set_page_config('Student Grade Prediction System')
# fig,ax = plt.subplots(figsize=(6,3))

# histogram = sns.histplot(df['final_exam_score'],kde=True,ax=ax)

# plt.savefig('IconsAndImages/exam_score_hist')
# st.pyplot(fig)

col1,col2 = st.columns([2,1])
col1.title('Student Grade Prediction System')
col2.markdown("""
    <div class='icon'>🎓</div>

    <style>
        .icon{
            font-size:90px;
        }
    </style>
""",unsafe_allow_html=True)

st.subheader('**🔖Introduction**',anchor='Introduction')
st.markdown("""
    <div class='intro'>
        <p>Our <strong>Grade Prediction System</strong> is designed to predict students’ academic performance using data such as study time, attendance, previous grades, and other factors. 
        It uses <strong>data analysis</strong> and <strong>machine learning</strong> to identify patterns in student performance.
        The system provides visual insights and predictions to help understand students’ academic progress.
        It aims to support students and educators in making data-driven academic decisions.</p>
    </div>
    <br>
    <style>
        .intro{
            border:1px solid gray;
            padding: 20px 20px;
            border-radius:10px;
        }
    </style>
""",unsafe_allow_html=True)

st.subheader('**🎯Project Objectives**',anchor='objectives')
st.markdown("""
    <br>
    <div class='objectives'>
        <div class='card1'>
            <p class='icon_labels'>🔮</p>
            Performance <br>Prediction
        </div>
        <div class='card2'>
            <p class='icon_labels'>🔍</p>
            Performance<br>Factors<br>Identification
        </div>
        <div class='card3'>
            <p class='icon_labels'>📈</p>
            Data<br>Analysis
        </div>
        <div class='card4'>
            <p class='icon_labels'>📊</p>
            Data<br>Visualization
        </div>
    </div>
    <br>

    <style>
        .objectives{
            display:flex;
            gap:10px;
        }

        .card1,.card2,.card3,.card4{
            border:1px solid gray;
            border-radius:15px;
            justify-content:center;
            height:200px;
            text-align:center;
            padding:20px 20px;
            width:300px;
            box-shadow:0 4px 10px lightgray;
            transition:0.3s;
        }

        .objectives .icon_labels{
            font-size:40px;
        }

        .card1:hover,.card2:hover,.card3:hover,.card4:hover{
            transform:translateY(-3px);
            box-shadow:0 8px 20px lightgray;
        }

    </style>
""",unsafe_allow_html=True)

st.subheader('📃DataSet',anchor='dataset')
df = pd.read_csv(r'C:\Users\Asus\Desktop\Projects\Dataset\cleaned_student_data.csv')

def randomizer():
    number = 5
    st.dataframe(df.sample(number))
randomizer_button = st.button(label='Randomize Data',on_click=randomizer())

st.subheader('**📖Libraries**',anchor='libraries')
st.write('')
st.markdown("""
    <div class='tab'>
        <table>
            <tr>
                <th>S.N.</th>
                <th>Libraries</th>
                <th>Modules</th>
            </tr>
            <tr>
                <td class='sn'>1</td>
                <td>Category Encoders</td>
                <td>-</td>
            </tr>
            <tr>
                <td class='sn'>2</td>
                <td>Joblib</td>
                <td>-</td>
            </tr>
            <tr>
                <td class='sn'>3</td>
                <td>Matplotlib</td>
                <td>.pyplot</td>
            </tr>
            <tr>
                <td class='sn'>4</td>
                <td>Pandas</td>
                <td>-</td>
            </tr>
            <tr>
                <td class='sn'>5</td>
                <td>Seaborn</td>
                <td>-</td>
            </tr>
            <tr>
                <td class='sn'>6</td>
                <td>Sklearn</td>
                <td>
                    .compose<br>
                    .neighbors<br>
                    .linear_model<br>
                    .model_selection<br>
                    .preprocessing<br>
                    .svm<br>
                </td>
            </tr>
            <tr>
                <td class='sn'>7</td>
                <td>Streamlit</td>
                <td>-</td>
            </tr>
        </table>
    </div>

    <style>
        td{
            width:250px;
        }
        
        th{
            background-color:rgba(0,0,0,0.09)
        }

        tr:nth-child(odd){
            background-color:rgba(0,0,0,0.05)
        }

    </style>
""",unsafe_allow_html=True)

st.write('')
st.subheader('**⚙️Models Trained**',anchor='models')

st.markdown("""
    <div class = 'KNN'>
        <p class = 'num'>1️⃣</p>
        <div class= 'text'>
            <p class = 'title1'>
                <strong>🔍KNN Regressor</strong>
            </p>
            <p>
                K-Nearest Neighbors Regressor (KNN) predicts a student's numerical score by looking at the scores of the most similar students in the training data.<br>
                <br>
                Works based on : Distance between data points.
            </p>
        </div>
    </div>

    <div class ='linear'>
        <p class = 'num'>2️⃣</p>
        <div class = 'text'>
            <p class = 'title1'>
                <strong>📈Linear Model</strong>
            </p>
            <p>
                Linear Regression predicts a numerical score by finding a linear relationship between student features and the final exam score.<br>
                <br>
                Works well when relationships between features and the target are approximately linear.
            </p>
        </div>
    </div>

    <div class ='SVR'>
        <p class = 'num'>3️⃣</p>
        <div class = 'text'>
            <p class = 'title1'>
                <strong>🌀SVR Model</strong>
            </p>
            <p>
                Linear Regression predicts a numerical score by finding a linear relationship between student features and the final exam score.<br>
                <br>
                Works well when relationships between features and the target are approximately linear.
            </p>
        </div>
    </div>

    <style>

        .KNN .num{
            font-size:90px;
            padding:20px 10px;
        }

        .KNN .title1{
            font-size:25px;
        }
        .KNN{
            padding:20px 20px;
            display:flex;
            gap:60px;
            flex:1;
            border:1px solid black;
            border-radius:10px;
            box-shadow: 0 2px 10px lightgrey;
            margin-bottom:20px;
            transition:0.3s;
        }

        .linear .num{
            font-size:90px;
            padding:20px 10px;
        }
        
        .linear .title1{
            font-size:25px;
        }

        .linear{
            padding:20px 20px;
            display:flex;
            gap:60px;
            flex:1;
            border:1px solid black;
            border-radius:10px;
            box-shadow: 0 2px 10px lightgrey;
            margin-bottom:20px;
            transition:0.3s;
        }

        .SVR .num{
            font-size:90px;
            padding:20px 10px;
        }
    
        .SVR .title1{
            font-size:25px;
        }
        
        .SVR{
            padding:20px 20px;
            display:flex;
            gap:60px;
            flex:1;
            border:1px solid black;
            border-radius:10px;
            box-shadow: 0 2px 10px lightgrey;
            margin-bottom:20px;
            transition:0.3s;
        }

        .KNN:hover,.linear:hover,.SVR:hover{
            transform:translateY(-1px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }
    </style>

    <br>
""",unsafe_allow_html=True)

st.subheader('**⚽Project Goal**',anchor='goal')
st.markdown("""
    <div class='goal'>
        <p class = 'goal_text'>
            The main goal of this project is to 
            <strong>demonstrate how machine learning and data analysis can be used to understand student performance and provide meaningful academic predictions.</strong>
        </p>
    </div>

    <style>
        .goal{
            border: 1px solid gray;
            padding:20px 20px;
            border-radius:10px;
        }


    </style>
""",unsafe_allow_html=True)

st.markdown("""
    <div class='footer'>
        <div class='footer-column1'>
            <a href = '#Introduction'>📌Introduction</a>
            <a href = '#objectives'>🎯Objectives</a>
            <a href = '#dataset'>📃Data Set</a>
            <a href = '#libraries'>📖Libraries</a>
            <a href = '#models'>⚙️Models</a>
            <a href = '#goal'>⚽Project Goal</a>

    </div>

    <style>
        .footer-column1 a{
            display:flex;
            flex-direction:column;
            text-decoration:None;
            color:white;
            font-size:12px;
        }

        .footer{
            margin-top:20px;
            display:flex;
            gap:200px;
            background-color:black;
            padding:20px 20px;
        }

    </style>

    <div class = 'footer-column2'>
        <a href = 'mailto:aadritthapa01@gmail.com'>✉️Email</a>
        <a href = '#'>📞Contact Us</a>
    </div>

    <div class = 'footer-column3'>
        <a href = 'https://github.com/Codeharbor-01/Project'>
            🔗Github
        </a>
    </div>

    <style>
        .footer-column2 a,.footer-column3 a{
            display:flex;
            flex-direction:column;
            text-decoration:None;
            color:white;
            font-size:12px;
        }
    </style>
""",unsafe_allow_html=True)