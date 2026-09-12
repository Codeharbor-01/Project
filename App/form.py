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

    study_hours = st.number_input(label='**Study Hours**',step=1,min_value=0,max_value=24)
    std_hrs_error = st.empty()

    attendance_percentage = st.number_input(label='**Attendance Percent**',min_value=0,max_value=100,step=1)
    percent_error = st.empty()

    sleep_hours = st.number_input(label='**Sleep Hours**',step=1,min_value=0,max_value=24)
    sleep_hrs_error = st.empty()

    parental_education = st.selectbox(label='**ParentalEducation**',options=['High School','Bachelors','Masters','PhD'])
    edu_error = st.empty()

    multi_options = st.multiselect(label='**Availability**',options=['Internet Access','Extracurricular Activities','Part Time Job'],placeholder='Please select available options only.')

    previous_grade = st.number_input(label='**Previous Grade**',step=0.1,min_value=0.0,max_value=100.0)
    grade_error = st.empty()

    submitted = st.form_submit_button(label='Submit')

    if submitted:
        if not (fN or lN):
            fN_error.error('First name and Last name is required.')

        with st.status('Submitting Form...') as status:
            time.sleep(3)
            status.update(label='Form Submitted Successfully!✅',state='complete')

st.divider()