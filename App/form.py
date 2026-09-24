import joblib
import pandas as pd
import streamlit as st
import time

logo_img = '📚'
st.logo(
    logo_img,
)
st.title('Student Grade Prediction Form')

st.text('Please fill the form below to calculate the final grade.')
#previous_grade	final_exam_score	final_grade
with st.form('Student Grade Prediction Form'):
    id = st.number_input(label='**Student ID**',step=1,min_value=1,max_value=None)

    col1,col2,col3 = st.columns(3)
    fN  = col1.text_input(label='**First Name**',placeholder='John')
    fN_error = st.empty()

    mN  = col2.text_input(label='**Middle Name**',placeholder='Michael')
    mN_error= st.empty()

    lN  = col3.text_input(label='**Last Name**',placeholder='Howell')
    lN_error = st.empty()

    gender = st.selectbox(label='**Gender**',options=['Male','Female','Other'])
    gender_error = st.empty()

    age = st.number_input(label='**Age**',min_value=18,max_value=30)
    age_error = st.empty()

    major = st.selectbox(label='**Major**',options=['Business','Computer Science','Economics','Engineering','Mathematics','Psychology'])
    major_error = st.empty()

    study_hours = st.number_input(label='**Study Hours**',step=1,min_value=0,max_value=14)
    std_hrs_error = st.empty()

    attendance_percentage = st.number_input(label='**Attendance Percent**',min_value=0,max_value=100,step=1)
    percent_error = st.empty()

    sleep_hours = st.number_input(label='**Sleep Hours**',step=1,min_value=0,max_value=10)
    sleep_hrs_error = st.empty()

    social_interaction_hours = st.number_input(label='**Social Interaction Hours (Weekly)**',min_value=0,max_value=20)
    social_error = st.empty()

    previous_cgpa = st.number_input(label='**Previous CGPA (0-4)**',step=1.00,min_value=0.00,max_value=4.00)
    grade_error = st.empty()

    submitted = st.form_submit_button(label='Submit')
    success=False

    if submitted:
        if not (fN or lN):
            fN_error.error('First name and Last name is required.')

        if not 0<study_hours<=10:
            std_hrs_error.error('Study hour exceeds the range of 0 to 10.')

        if not sleep_hours:
            sleep_hrs_error.error('Field cannot be empty.')
        elif not 3<=sleep_hours<=10:
            sleep_hrs_error.error('Sleep hour exceeds the range of 3 to 10')

        fields = [fN,lN,age,gender,major,study_hours,attendance_percentage,sleep_hours,social_interaction_hours,previous_cgpa]

        if not all(fields):
            st.error('Error submitting form. Please fill the required fields.')
        else:
            with st.status('Submitting Form...') as status:
                time.sleep(3)
                status.update(label='Form Submitted Successfully!✅',state='complete')

user_data={
    'Gender':[gender],
    'Age':age,
    'Major':major,
    'Attendance_Pct':attendance_percentage,
    'Study_Hours_Per_Day':study_hours,
    'Previous_CGPA':previous_cgpa,
    'Sleep_Hours':sleep_hours,
    'Social_Hours_Week':social_interaction_hours
}

user_df = pd.DataFrame(user_data)
if submitted:

    st.divider()
    st.header('Prediction')
    st.warning("⚠️The following prediction is just the estimated outcome. Results may vary on user's hardwork and action.")

    linear_model = joblib.load(r'Pkl_Files/LinearModel.pkl')
    KNN_model = joblib.load(r'Pkl_Files/KNNRegressionModel.pkl')
    SVR_model = joblib.load(r'Pkl_Files/SVRModel.pkl')
    RandomForest_model = joblib.load(r'Pkl_Files\RandomForestModel.pkl')

    linear_scores = joblib.load(r'Scores/Linear_Score.pkl')
    KNN_scores = joblib.load(r'Scores/KNN_Score.pkl')
    SVR_scores = joblib.load(r'Scores/SVR_Scores.pkl')
    RandomForest_scores = joblib.load(r'Scores\RandomForest_Scores.pkl')

    model_li = [linear_model,KNN_model,SVR_model,RandomForest_model]
    model_scores = [linear_scores,KNN_scores,SVR_scores,RandomForest_scores]
    best_score = max(model_scores,key=lambda x:x['r2'])
    best_score_index = model_scores.index(best_score)
    best_model = model_li[best_score_index]

    prediction = best_model.predict(user_df)

    container_box = st.container(border=True)
    container_box.markdown(f"""
        <div class='title'>
            <h3>Prediction Result</h3>
        </div>

        <p class='col1'>
            <strong>Student ID : </strong> {id}
        </p>

        <div class='columns'>
            <p class='col1'>
                <strong>Name : </strong>{fN} {mN} {lN}
            </p>
            <p class='col1'>
                <strong>Gender : </strong> {gender}
            </p>
                        
        </div>


        <div class='details'>
            <h4>Student Details</h4>
        </div>

        <div class = 'res_table'>
            <table>
                <tr>
                    <th>Major</th>
                    <td>{major}</td>
                </tr>
                <tr>
                    <th>Study Hours</th>
                    <td>{study_hours}</td>
                </tr>
                <tr>
                    <th>Attendance Percent</th>
                    <td>{attendance_percentage}%</td>
                </tr>
                <tr>
                    <th>Sleep Hours</th>
                    <td>{sleep_hours}</td>
                </tr>
                <tr>
                    <th>Social Interaction Hours</th>
                    <td>{social_interaction_hours}</td>
                </tr>
                <tr>
                    <th>Previous CGPA</th>
                    <td>{previous_cgpa}</td>
                </tr>
            </table>
        </div>

        <div class='bottom_cols'>
            <p><strong>Perfect Score &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : </strong> 4.00</p>
            <p><strong>Estimated CGPA : </strong>{prediction[0].round(2)}</p>
        </div>

        <style>
            .title{{
                text-align:center;
            }}

            .res_table table{{
                width:100%;
            }}

            .columns{{
                display:flex;
                gap:400px;
            }}

            .details{{
                margin-top:5px;
            }}

            .bottom_cols p{{
                text-align:left;
                padding-left:72%;
                margin:4px 0;
            }}

            .bottom_cols p:last-child{{
                padding-bottom:10px;
            }}

            .res_table table tr:nth-child(odd){{
                background-color:rgba(0,0,0,0.09)
            }}
        </style>
""",unsafe_allow_html=True)