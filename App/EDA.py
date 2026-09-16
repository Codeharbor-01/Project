import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

uncleaned_file_path = r'C:\Users\Asus\Desktop\Projects\Dataset\student_performance_dataset.csv'
uncleaned_df = pd.read_csv(uncleaned_file_path)

cleaned_file_path = r'C:\Users\Asus\Desktop\Projects\Dataset\cleaned_student_data.csv'
df = pd.read_csv(cleaned_file_path)

st.title('EDA Report',anchor='title')
st.text('This section provides an overview of the student performance dataset, including its structure, variables, and basic statistical information.')

tab1,tab2,tab3 = st.tabs(["Overview",'Analysis','Findings'])

tab1.header('Data Overview')
tab1.text('The below table shows the report of the initial (uncleaned) dataset.')
col1,col2 = tab1.columns(2)
col1.markdown(f"""
    <h4>Dataset Statistics</h4>
    <div class='features'>
        <table>
            <tr>
                <th>Number of Variables</th>
                <td>{len(uncleaned_df.columns)}</td>
            </tr>
            <tr>
                <th>Number of observations</th>
                <td>{len(uncleaned_df)}</td>
            </tr>
            <tr>
                <th>Missing cells</th>
                <td>{(uncleaned_df.isna().sum().sum())}</td>
            </tr>
            <tr>
                <th>Missing cells (%)</th>
                <td>{(((uncleaned_df.isna().sum().sum()))/(len(uncleaned_df)))*100}%</td>
            </tr>
            <tr>
                <th>Duplicate rows</th>
                <td>{uncleaned_df.duplicated().sum()}</td>
            </tr>
            <tr>
                <th>Duplicate rows (%)</th>
                <td>{(uncleaned_df.duplicated().sum()/len(uncleaned_df))*100}%</td>
            </tr>
            <tr>
                <th>Total size in memory</th>
                <td>{os.path.getsize(uncleaned_file_path)/1024:.2f} KB</td>
            </tr>
        </table>
    </div>

    <style>

        tr:nth-child(odd){{
            background-color:rgba(0,0,0,0.09);
        }}

    </style>
""",unsafe_allow_html=True)

col2.markdown(f"""
    <div class='vartypes'>
        <h4>Variable Types</h4>
        <table>
            <tr>
                <th>Numerical</th>
                <td>{uncleaned_df.select_dtypes(['int','float']).shape[1]}</td>
            </tr>
            <tr>
                <th>Categorical</th>
                <td>{uncleaned_df.select_dtypes('str').shape[1]}</td>
            </tr>
        </table>
    </div>
""",unsafe_allow_html=True)

tab1.divider()
tab1.text('The table below shows the report of the final (cleaned) dataset.')
col3,col4 = tab1.columns(2)
col3.markdown(f"""
    <h4>Dataset Statistics</h4>
    <div class='features'>
        <table>
            <tr>
                <th>Number of Variables</th>
                <td>{len(df.columns)}</td>
            </tr>
            <tr>
                <th>Number of observations</th>
                <td>{len(df)}</td>
            </tr>
            <tr>
                <th>Missing cells</th>
                <td>{df.isna().sum().sum()}</td>
            </tr>
            <tr>
                <th>Missing cells (%)</th>
                <td>{((df.isna().sum().sum())/(len(df)))*100}%</td>
            </tr>
            <tr>
                <th>Duplicate rows</th>
                <td>{df.duplicated().sum()}</td>
            </tr>
            <tr>
                <th>Duplicate rows (%)</th>
                <td>{(df.duplicated().sum()/len(df))*100}%</td>
            </tr>
            <tr>
                <th>Total size in memory</th>
                <td>{os.path.getsize(cleaned_file_path)/1024:.2f} KB</td>
            </tr>
        </table>
    </div>

    <style>

        tr:nth-child(odd){{
            background-color:rgba(0,0,0,0.09);
        }}

    </style>
""",unsafe_allow_html=True)

col4.markdown(f"""
    <div class='vartypes'>
        <h4>Variable Types</h4>
        <table>
            <tr>
                <th>Numerical</th>
                <td>{df.select_dtypes(['int','float']).shape[1]}</td>
            </tr>
            <tr>
                <th>Categorical</th>
                <td>{df.select_dtypes('str').shape[1]}</td>
            </tr>
        </table>
    </div>
""",unsafe_allow_html=True)

tab2.header("Data Analysis",anchor='analysis')
st.markdown("""

""")
fig1,ax = plt.subplots()
tab2.subheader('Gender vs Final Exam Score')
gender_avg = df.groupby('gender').agg(
        Average_Final_Exam_Score = ('final_exam_score','mean')
    ).reset_index()

tab2.dataframe(gender_avg.round(2),hide_index=True)

ax.set_title('Gender vs Final Exam Score')
ax.set_xlabel('Gender')
ax.set_ylabel('Avg Final Exam Score')
sns.barplot(gender_avg,x='gender',y='Average_Final_Exam_Score',ax=ax)
tab2.pyplot(fig1)
tab2.divider()

tab2.subheader('Parental Education vs Final Exam Score')
parental_edu_avg =  df.groupby('parental_education').agg(
        Average_Final_Exam_Score = ('final_exam_score','mean')
    ).reset_index()

tab2.dataframe(parental_edu_avg.round(2),hide_index=True)

fig2,ax = plt.subplots()
ax.set_title('Parental Education vs Final Exam Score')
ax.set_xlabel('Parental Education')
ax.set_ylabel('Final Exam Score')
sns.barplot(parental_edu_avg,x='parental_education',y='Average_Final_Exam_Score',ax=ax)
tab2.pyplot(fig2)
tab2.divider()

tab2.subheader('Comparison of Study time and Final Exam Score')
study_and_avg_final_score = df.groupby(['study_time_hours']).agg(
       Average_final_exam_score = ('final_exam_score','mean')
    ).reset_index()

tab2.dataframe(study_and_avg_final_score.round(2),hide_index=True)

fig3,ax = plt.subplots()
ax.set_title('Study Time vs Final Exam Score')
ax.set_xlabel('Study Time (in hours)')
ax.set_ylabel('Average Final Exam Score')
sns.scatterplot(study_and_avg_final_score,x='study_time_hours',y='Average_final_exam_score',ax=ax)
tab2.pyplot(fig3)
tab2.divider()

tab2.subheader('Impact of Attendance on Final Exam Score')
tab2.dataframe(
    df.groupby('attendance_percent')['final_exam_score'].mean()
)

fig4,ax = plt.subplots()
ax.set_title('Attendance Percent vs Final Exam Score')
ax.set_xlabel('Attendance Percent')
ax.set_ylabel('Average Final Exam Score')
sns.scatterplot(df,x='attendance_percent',y='final_exam_score',ax=ax)
tab2.pyplot(fig4)
tab2.divider()

tab2.subheader('Previous Grade vs Final Exam Score')
avg_prev_vs_avg_final_grade = df.groupby('study_time_hours').agg(
        Average_Previous_Grade = ('previous_grade','mean'),
        Average_Final_Exam_Score = ('final_exam_score','mean')
    ).sort_values(by='study_time_hours',ascending=True)
tab2.dataframe(avg_prev_vs_avg_final_grade.round(2),hide_index=True)

fig5,ax = plt.subplots(2,1)

ax[0].set_title('Trend of study time and final exam score')
ax[0].set_xlabel('Study Time (in hours)')
ax[0].set_ylabel('Average Final Exam Score')
sns.lineplot(avg_prev_vs_avg_final_grade,x='study_time_hours',y='Average_Final_Exam_Score',ax=ax[0])

ax[1].set_title('Trend of study time and previous grade')
ax[1].set_xlabel('Study Time (in hours)')
ax[1].set_ylabel('Average Previous Grade')
sns.lineplot(avg_prev_vs_avg_final_grade,x='study_time_hours',y='Average_Previous_Grade',ax=ax[1])
plt.tight_layout()
plt.subplots_adjust(hspace=1)
tab2.pyplot(fig5)
tab2.divider()
tab2.subheader('Gender vs Internet Access')

gender_vs_internet_access = df.groupby(['gender','internet_access']).size().reset_index(name='Number of Students')

tab2.dataframe(gender_vs_internet_access,hide_index=True)
fig6,ax = plt.subplots()
ax.set_xlabel('Gender')
sns.barplot(gender_vs_internet_access,x='gender',y='Number of Students',hue='internet_access')
tab2.pyplot(fig6)
tab2.divider()

tab2.subheader("Numerical Columns' Heatmap")
numerical_cols = df.select_dtypes(['int','float']).corr()

fig7,ax = plt.subplots()
sns.heatmap(numerical_cols,annot=True,cmap='coolwarm',fmt='.2f',ax=ax)
tab2.pyplot(fig7)
tab2.divider()

tab2.subheader('Final Exam Score Distribution')
fig8,ax = plt.subplots()
sns.histplot(df,x='final_exam_score',bins=10,kde=True,ax=ax)

ax.set_xlabel('Final Exam Score')
ax.set_ylabel('Number of students')
tab2.pyplot(fig8)

tab3.header('Findings')
tab3.subheader('1. Overall Academic Performance')

tab3.markdown(f"""
<div class='academic_performance'>
    <table>
        <tr>
            <th>Measure</th>
            <th>Previous Grade</th>
            <th>Final Exam Score</th>
        </tr>
        <tr>
            <th>Mean</th>
            <td>{df['previous_grade'].mean().round(2)}</td>
            <td>{df['final_exam_score'].mean().round(2)}</td>
        </tr>
        <tr>
            <th>Minimum</th>
            <td>{df['previous_grade'].min()}</td>
            <td>{df['final_exam_score'].min()}</td>
        </tr>
        <tr>
            <th>Maximum</th>
            <td>{df['previous_grade'].max()}</td>
            <td>{df['final_exam_score'].max()}</td>
        </tr>
        <tr>
            <th>Standard Deviation</th>
            <td>{df['previous_grade'].std().round(2)}</td>
            <td>{df['final_exam_score'].std().round(2)}</td>
        </tr>
    </table>
</div>

<style>
    .academic_performance table{{
        width:100%;
    }}
</style>
""",unsafe_allow_html=True)
tab3.divider()

tab3.subheader('2. Student Background Summary')
tab3.markdown('The table below shows the count of students with **Internet Access** and involved in **Part time job** and **Extracurricular activites**.')
performance_table = {
    'Values':[True,False],
    'Internet Access':df['internet_access'].value_counts(),
    'Part-Time Job':df['part_time_job'].value_counts(),
    'Extracurricular Activities':df['extracurricular_activities'].value_counts()
}

tab3.dataframe(performance_table)
tab3.divider()

tab3.subheader('3. Correlation Analysis')
tab3.markdown('This section examines the relationships between selected numerical variables in the dataset. ' \
'The correlation values help identify the strength and direction of relationships between factors such as study time, attendance, sleep hours, previous grades, and final exam scores.')
correlation_table = numerical_cols.corr()
tab3.dataframe(correlation_table)