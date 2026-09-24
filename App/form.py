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

    study_hours = st.number_input(label='**Study Hours**',step=1,min_value=0,max_value=10)
    std_hrs_error = st.empty()

    attendance_percentage = st.number_input(label='**Attendance Percent**',min_value=0,max_value=100,step=1)
    percent_error = st.empty()

    sleep_hours = st.number_input(label='**Sleep Hours**',step=1,min_value=0,max_value=10)
    sleep_hrs_error = st.empty()

    parental_education = st.selectbox(label='**ParentalEducation**',options=['High School','Bachelors','Masters','PhD'])
    edu_error = st.empty()

    multi_options = st.multiselect(label='**Availability**',options=['Internet Access','Extracurricular Activities','Part Time Job'],placeholder='Please select available options only.')
    internet = 'Internet Access' in multi_options
    eca = 'Extracurricular Activities' in multi_options
    part_time_job = 'Part Time Job' in multi_options

    previous_grade = st.number_input(label='**Previous Grade (0-100)**',step=0.1,min_value=0.0,max_value=100.0)
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

        fields = [fN,lN,gender,study_hours,attendance_percentage,sleep_hours,parental_education,previous_grade]

        if not all(fields):
            st.error('Error submitting form. Please fill the required fields.')
        else:
            with st.status('Submitting Form...') as status:
                time.sleep(3)
                status.update(label='Form Submitted Successfully!✅',state='complete')
            st.divider()

user_data={
    'gender':[gender],
    'study_time_hours':study_hours,
    'attendance_percent':attendance_percentage,
    'sleep_hours':sleep_hours,
    'parental_education':parental_education,
    'internet_access':[internet],
    'extracurricular_activities':[eca],
    'part_time_job':[part_time_job],
    'previous_grade':previous_grade
}

user_df = pd.DataFrame(user_data)
if True:
    st.header('Prediction')
    st.warning("⚠️The following prediction is just the estimated outcome. Results may vary on user's hardwork and action.")

    linear_model = joblib.load('Pkl_Files/LinearModel.pkl')
    KNN_model = joblib.load('Pkl_Files/KNNRegressionModel.pkl')
    SVR_model = joblib.load('Pkl_Files/SVRModel.pkl')

    linear_scores = joblib.load('Scores/Linear_Score.pkl')
    KNN_scores = joblib.load('Scores/KNN_Score.pkl')
    SVR_scores = joblib.load('Scores/SVR_Scores.pkl')

    model_li = [linear_model,KNN_model,SVR_model]
    st.text(linear_scores)
    st.text(KNN_scores)
    st.text(SVR_scores)

#     container_box = st.container(border=True)
#     container_box.markdown(f"""
#         <div class='title'>
#             <h3>Prediction Result</h3>
#         </div>

#         <p class='col1'>
#             <strong>Student Id : </strong> {id}
#         </p>

#         <div class='columns'>
#             <p class='col1'>
#                 <strong>Name : </strong>{fN} {mN} {lN}
#             </p>
#             <p class='col1'>
#                 <strong>Gender : </strong> {gender}
#             </p>
                        
#         </div>


#         <div class='details'>
#             <h4>Student Details</h4>
#         </div>

#         <div class = 'res_table'>
#             <table>
#                 <tr>
#                     <th>Study Hours</th>
#                     <td>{study_hours}</td>
#                 </tr>
#                 <tr>
#                     <th>Attendance Percent</th>
#                     <td>{attendance_percentage}%</td>
#                 </tr>
#                 <tr>
#                     <th>Sleep Hours</th>
#                     <td>{sleep_hours}</td>
#                 </tr>
#                 <tr>
#                     <th>Parental Education</th>
#                     <td>{parental_education}</td>
#                 </tr>
#                 <tr>
#                     <th>Availability</th>
#                     <td>{'<br>'.join(multi_options)}</td>
#                 </tr>
#                 <tr>
#                     <th>Previous Grade</th>
#                     <td>{previous_grade}</td>
#                 </tr>
#             </table>
#         </div>

#         div class='bottom_cols'>
#             <p><strong>Perfect Score &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : </strong> 100%</p>
#             <p><strong>Pass Score &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : </strong>40%</p>
#             <p><strong>Estimated Score : </strong>{prediction}%</p>
#             <p><strong>Estimated GPA &nbsp;&nbsp; : </strong>{(prediction/100)*4:.2f}
#         </div>

#         <style>
#             .title{{
#                 text-align:center;
#             }}

#             .res_table table{{
#                 width:100%;
#             }}

#             .columns{{
#                 display:flex;
#                 gap:400px;
#             }}

#             .details{{
#                 margin-top:5px;
#             }}

#             .bottom_cols p{{
#                 text-align:left;
#                 padding-left:72%;
#                 margin:4px 0;
#             }}

#             .bottom_cols p:last-child{{
#                 padding-bottom:10px;
#             }}

#             .res_table table tr:nth-child(odd){{
#                 background-color:rgba(0,0,0,0.09)
#             }}
#         </style>
# """,unsafe_allow_html=True)