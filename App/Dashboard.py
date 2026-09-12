import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

st.subheader('**Libraries**',anchor='libraries')
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
st.subheader('**Models Trained**',anchor='models')
