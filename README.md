# 🎓 AI-Powered Student Performance Prediction System

## 📌 Project Overview

The **AI-Powered Student Performance Prediction System** is a Machine Learning-based web application that predicts a student's expected final academic performance.

The system analyzes important academic factors such as **attendance, study hours, previous marks, assignment marks, internal marks, and class participation**. A trained **Random Forest Regression** model uses these factors to predict the student's final marks.

The application is developed using **Python and Streamlit**, providing a simple and interactive interface for students and educators.

---

## 🎯 Objectives

- Predict students' expected final academic marks.
- Analyze factors that influence student performance.
- Identify students who may need additional academic support.
- Provide performance-based recommendations.
- Demonstrate the application of Machine Learning in education.

---

## ✨ Features

### 🏠 Home
- Project introduction
- Project objectives
- Key features
- System workflow

### 📊 Performance Prediction
Users can enter:

- Attendance percentage
- Study hours per day
- Previous examination marks
- Assignment marks
- Internal marks
- Class participation

The system predicts the student's expected final marks.

### 📈 Performance Analysis

The application displays:

- Predicted final marks
- Performance level
- Academic input summary
- Performance visualization
- Personalized recommendation

### ℹ️ About Project

Provides information about:

- Project
- Machine Learning model
- Input features
- Technologies used
- Model performance

---

## 🧠 Machine Learning Model

The system uses **Random Forest Regression** to predict the student's final marks.

### Input Features

| Feature | Description |
|---|---|
| Attendance | Student attendance percentage |
| Study Hours | Average study hours per day |
| Previous Marks | Previous examination marks |
| Assignment Marks | Assignment performance |
| Internal Marks | Internal examination marks |
| Participation | Classroom participation level |

### Target Variable

**Final Marks**

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**
- **Streamlit**
- **Pickle**

---

## 📁 Project Structure

```text
AI-Powered Student Performance Prediction System/
│
├── data/
│   └── student_data.csv
│
├── models/
│   └── student_performance_model.pkl
│
├── venv/
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
