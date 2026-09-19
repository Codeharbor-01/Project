import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from category_encoders import BinaryEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

df = pd.read_csv(r'C:\Users\Asus\Desktop\Projects\Dataset\cleaned_student_data.csv')

x = df.drop(columns=['student_id','final_exam_score','final_grade'])
y = df['final_exam_score']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

num_columns = ['study_time_hours','attendance_percent','sleep_hours','previous_grade']
ord_columns = ['parental_education']
nom_columns = ['gender']
bool_columns = ['internet_access','extracurricular_activities','part_time_job','Pass']

education_order = ['High School','Bachelors','Masters','PhD']

preprocessor = ColumnTransformer(
    transformers=[
        ('num_scaled',StandardScaler(),num_columns),
        ('ord_encoded',OrdinalEncoder(categories=[education_order]),ord_columns),
        ('nom_encoded',BinaryEncoder(),nom_columns)
    ],remainder='passthrough'
)

pipe = Pipeline(
    steps=[
        ('preprocessing',preprocessor),
        ('regressor',SVR())
    ]
)

params = {
    'regressor__C':range(1,21),
    'regressor__kernel':['linear','rbf','poly']
}

grid_model = GridSearchCV(pipe,param_grid=params,cv=10,scoring='r2')
grid_model.fit(x_train,y_train)

best_model = grid_model.best_estimator_

def get_SVR_score():

    SVR_score = grid_model.best_score_
    return SVR_score

joblib.dump(best_model,'Pkl_Files/SVRModel.pkl')