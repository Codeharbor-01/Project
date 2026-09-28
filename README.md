# 🎓 Student CGPA Prediction System

A machine learning-based **Student CGPA Prediction System** built with Python and Streamlit. The system analyzes student academic and personal factors, applies trained machine learning models, and provides an estimated academic performance through an interactive web application.

## 🚀 Live Demo

🌐 **Streamlit App:**
https://student-cgpa-prediction-system.streamlit.app/

## 📌 Project Overview

The **Student CGPA Prediction System** is designed to demonstrate how machine learning can be applied to student performance prediction.

Users can enter information such as:

* Student ID
* Gender
* Study time
* Attendance percentage
* Sleep hours
* Parental education
* Internet access
* Extracurricular activities
* Part-time job
* Previous grade

The system processes these inputs through a machine learning pipeline and generates a predicted academic score and estimated GPA.

## ✨ Features

### 📊 Dashboard

Provides an overview of the student dataset, including:

* Dataset preview
* Dataset information
* Statistical summaries
* Academic performance metrics

### 📄 Student Prediction Form

Users can enter student information through an interactive form and receive a predicted result.

The prediction section includes:

* Predicted final examination score
* Estimated GPA
* Student information summary
* Downloadable prediction report

### 📈 EDA Report

The Exploratory Data Analysis section provides insights into the dataset through:

* Dataset statistics
* Missing-value analysis
* Academic performance analysis
* Distribution analysis
* Key findings

### ⚙️ Machine Learning Models

The project uses multiple regression algorithms to predict final examination scores, including:

* Linear Regression
* K-Nearest Neighbors Regression
* Support Vector Regression (SVR)

The trained models are evaluated and the model with the strongest validation performance is used for prediction.

### 🔍 Data Analysis

Provides interactive visualizations for exploring relationships and patterns within the student dataset.

## 🧠 Machine Learning Workflow

The project follows a typical machine learning workflow:

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Selection
     ↓
Data Preprocessing
     ↓
Feature Encoding
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Selection
     ↓
Prediction
```

## 🛠️ Technologies Used

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| Python            | Core programming language          |
| Pandas            | Data manipulation and analysis     |
| NumPy             | Numerical operations               |
| Matplotlib        | Data visualization                 |
| Seaborn           | Statistical visualization          |
| Scikit-learn      | Machine learning and preprocessing |
| Category Encoders | Categorical feature encoding       |
| Joblib            | Model serialization                |
| Streamlit         | Web application                    |
| Jupyter Notebook  | Data cleaning and experimentation  |

## 📂 Project Structure

```text
Student-CGPA-Prediction-System/
│
├── App/
│   ├── main.py
│   ├── Dashboard.py
│   ├── EDA.py
│   ├── form.py
│   ├── models.py
│   └── data_visualization.py
│
├── Dataset/
│   └── cleaned_student_data.csv
│
├── Pkl_Files/
│   ├── LinearModel.pkl
│   ├── KNNRegressionModel.pkl
│   └── SVRModel.pkl
│
├── Scores/
│   ├── Linear_Score.pkl
│   ├── KNN_Score.pkl
│   └── SVR_Score.pkl
│
├── model_files/
│   └── model training files
│
├── data_cleaning.ipynb
├── requirements.txt
└── README.md
```

## 📊 Dataset

The dataset contains information related to student academic performance and lifestyle/educational factors.

### Input Features

| Feature                      | Description                                 |
| ---------------------------- | ------------------------------------------- |
| `student_id`                 | Unique student identifier                   |
| `gender`                     | Student gender                              |
| `study_time_hours`           | Average study time                          |
| `attendance_percent`         | Attendance percentage                       |
| `sleep_hours`                | Average sleeping hours                      |
| `parental_education`         | Highest parental education level            |
| `internet_access`            | Availability of internet access             |
| `extracurricular_activities` | Participation in extracurricular activities |
| `part_time_job`              | Whether the student has a part-time job     |
| `previous_grade`             | Previous academic grade                     |

### Prediction Target

The primary prediction target is:

```text
final_exam_score
```

The predicted score is then used to provide an estimated GPA on a 4.0 scale.

## 🤖 Models

Three regression algorithms were explored:

### Linear Regression

Used as a baseline regression model to establish a reference performance.

### K-Nearest Neighbors Regression

Predicts a student's score based on the similarity between their features and other students in the training dataset.

### Support Vector Regression

Uses support vector machine principles to model relationships between student characteristics and final examination scores.

The models are trained using preprocessing pipelines containing appropriate numerical scaling and categorical encoding.

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Codeharbor-01/Student-CGPA-Prediction-System.git
```

### 2. Navigate into the project

```bash
cd Student-CGPA-Prediction-System
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run App/main.py
```

The application will then open in your browser.

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

When deploying the project, make sure that:

* `requirements.txt` is included in the repository.
* Dataset files are committed to GitHub.
* Model files are committed to GitHub.
* File paths are compatible with the deployment environment.
* Required Python packages use compatible versions with the saved machine learning models.

## 📈 Application Pages

The application contains the following main sections:

```text
📈 Dashboard
      ↓
📄 Prediction Form
      ↓
📊 EDA Report
      ↓
⚙️ Models
      ↓
🔍 Data Analysis
```

## 🎯 Project Objectives

The main objectives of this project are to:

1. Apply data preprocessing techniques to a real-world-style student dataset.
2. Explore factors associated with student academic performance.
3. Train and compare multiple regression models.
4. Build an interactive machine learning application.
5. Provide students with an estimated academic performance score.
6. Demonstrate the complete machine learning workflow from data preparation to deployment.

## ⚠️ Disclaimer

The predictions generated by this application are **estimates based on the dataset and trained machine learning models**. They should not be considered official academic results or guarantees of future performance.

## 👨‍💻 Contributors

**Codeharbor-01**

GitHub:
https://github.com/Codeharbor-01

## 📜 License

This project is intended for educational and academic purposes.
