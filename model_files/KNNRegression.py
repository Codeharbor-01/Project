import pandas as pd
import joblib

from sklearn.metrics import r2_score,mean_absolute_error,root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from category_encoders import BinaryEncoder
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV

df = pd.read_csv(r"C:\Users\Asus\Desktop\Projects\Dataset\cleaned_student_data.csv")

x = df.drop(columns=['Student_ID','Final_CGPA'])
y = df['Final_CGPA']

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42,test_size=0.2)

num_columns = [
    'Age',
    'Attendance_Pct',
    'Study_Hours_Per_Day',
    'Previous_CGPA',
    'Sleep_Hours',
    'Social_Hours_Week'
]
nom_columns = [
    'Gender',
    'Major'
]


preprocessor = ColumnTransformer(
    transformers=[
        ('num_scaled',StandardScaler(),num_columns),
        ('nom_encoded',BinaryEncoder(),nom_columns)
    ],remainder='passthrough'
)

pipe = Pipeline(
    steps=[
        ('preprocessing',preprocessor),
        ('regressor',KNeighborsRegressor())
    ]
)

params = {
    'regressor__n_neighbors': [2,3,5,7,9,11,15,20,25],
    'regressor__weights': ['uniform', 'distance'],
    'regressor__p': [1, 2]
}

grid_model = GridSearchCV(pipe,param_grid=params,cv=10,scoring='r2')
grid_model.fit(x_train,y_train)

best_model = grid_model.best_estimator_

y_pred = best_model.predict(x_test)

r2 = r2_score(y_test,y_pred)
mae = mean_absolute_error(y_test,y_pred)
rmse = root_mean_squared_error(y_test,y_pred)

scores = {
    'r2':r2,
    'mae':mae,
    'rmse':rmse
}

joblib.dump(best_model,'Pkl_Files/KNNRegressionModel.pkl')
joblib.dump(scores,"Scores/KNN_Score.pkl")