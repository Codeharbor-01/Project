import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from category_encoders import BinaryEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV

df = pd.read_csv(r"C:\Users\Asus\Desktop\Projects\Dataset\cleaned_student_data.csv")

x = df.drop(columns=['student_id','final_exam_score','final_grade'])
y = df['final_exam_score']

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42,test_size=0.2)

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
        ('regressor',LinearRegression())
    ]
)

param_grid = {
    'regressor__fit_intercept':[True,False],
    'regressor__positive':[True,False]
}

model = GridSearchCV(pipe,param_grid=param_grid,cv=5,scoring='r2')
model.fit(x_train,y_train)
best_model = model.best_estimator_
joblib.dump(best_model,'Pkl Files/LinearModel.pkl')
