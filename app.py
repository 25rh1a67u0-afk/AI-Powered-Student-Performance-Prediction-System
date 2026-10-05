import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="AI Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# =========================
# LOAD ML MODEL
# =========================

with open("models/student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)


# =========================
# SIDEBAR NAVIGATION
# =========================

st.sidebar.title("🎓 Student Performance")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📊 Prediction", "ℹ️ About Project"]
)


# =========================
# HOME PAGE
# =========================

if page == "🏠 Home":

    st.title("🎓 AI-Powered Student Performance Prediction System")

    st.subheader("Welcome!")

    st.write(
        """
        This project uses Artificial Intelligence and Machine Learning
        to predict a student's final academic performance.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            "📚\n\n"
            "### Academic Data\n\n"
            "Analyze important student performance factors."
        )

    with col2:
        st.success(
            "🤖\n\n"
            "### Machine Learning\n\n"
            "Use a trained Random Forest model for prediction."
        )

    with col3:
        st.warning(
            "📊\n\n"
            "### Prediction\n\n"
            "Predict the student's expected final marks."
        )

    st.divider()

    st.subheader("🎯 Project Objective")

    st.write(
        """
        The main objective of this system is to help identify student
        performance using factors such as attendance, study hours,
        previous marks, assignment marks, internal marks and
        classroom participation.
        """
    )


# =========================
# PREDICTION PAGE
# =========================

elif page == "📊 Prediction":

    st.title("📊 Student Performance Prediction")

    st.write(
        "Enter the student's information using the controls on the left."
    )

    st.divider()

    # Student inputs
    st.subheader("📚 Student Information")

    col1, col2 = st.columns(2)

    with col1:

        attendance = st.slider(
            "Attendance (%)",
            min_value=0,
            max_value=100,
            value=80
        )

        study_hours = st.slider(
            "Study Hours per Day",
            min_value=0,
            max_value=12,
            value=3
        )

        previous_marks = st.slider(
            "Previous Exam Marks",
            min_value=0,
            max_value=100,
            value=70
        )

    with col2:

        assignment_marks = st.slider(
            "Assignment Marks",
            min_value=0,
            max_value=100,
            value=70
        )

        internal_marks = st.slider(
            "Internal Marks",
            min_value=0,
            max_value=100,
            value=70
        )

        participation = st.slider(
            "Class Participation",
            min_value=0,
            max_value=10,
            value=5
        )

    st.divider()

    # Create input data
    input_data = pd.DataFrame({
        "attendance": [attendance],
        "study_hours": [study_hours],
        "previous_marks": [previous_marks],
        "assignment_marks": [assignment_marks],
        "internal_marks": [internal_marks],
        "participation": [participation]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # Keep prediction between 0 and 100
    prediction = max(0, min(100, prediction))

    # Performance category
    if prediction >= 85:

        category = "Excellent"
        message = "The student is performing very well."

    elif prediction >= 70:

        category = "Good"
        message = "The student is showing good performance."

    elif prediction >= 50:

        category = "Average"
        message = "The student may need some improvement."

    else:

        category = "At Risk"
        message = "The student needs additional academic support."

    # =========================
    # RESULT
    # =========================

    st.subheader("📊 Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Predicted Final Marks",
            f"{prediction:.1f}%"
        )

    with col2:

        st.metric(
            "Performance Level",
            category
        )

    with col3:

        if prediction >= 85:

            st.success("🌟 Excellent")

        elif prediction >= 70:

            st.success("✅ Good Performance")

        elif prediction >= 50:

            st.warning("⚠️ Average")

        else:

            st.error("🚨 At Risk")

    st.info(message)

    st.divider()

    # =========================
    # STUDENT SUMMARY
    # =========================

    st.subheader("📝 Student Information")

    summary = pd.DataFrame({
        "Parameter": [
            "Attendance",
            "Study Hours",
            "Previous Marks",
            "Assignment Marks",
            "Internal Marks",
            "Participation"
        ],

        "Value": [
            f"{attendance}%",
            f"{study_hours} hours/day",
            f"{previous_marks}%",
            f"{assignment_marks}%",
            f"{internal_marks}%",
            f"{participation}/10"
        ]
    })

    st.table(summary)

    # =========================
    # PERFORMANCE CHART
    # =========================

    st.subheader("📈 Student Performance Factors")

    chart_data = pd.DataFrame({

        "Factor": [
            "Attendance",
            "Previous Marks",
            "Assignment Marks",
            "Internal Marks",
            "Participation"
        ],

        "Score": [
            attendance,
            previous_marks,
            assignment_marks,
            internal_marks,
            participation * 10
        ]
    })

    fig, ax = plt.subplots()

    sns.barplot(
        data=chart_data,
        x="Factor",
        y="Score",
        ax=ax
    )

    ax.set_ylim(0, 100)
    ax.set_ylabel("Score")
    ax.set_xlabel("")

    plt.xticks(rotation=20)

    st.pyplot(fig)

    # =========================
    # RECOMMENDATIONS
    # =========================

    st.subheader("💡 Recommendations")

    recommendations = []

    if attendance < 75:

        recommendations.append(
            "Improve attendance and attend classes regularly."
        )

    if study_hours < 3:

        recommendations.append(
            "Increase daily study time."
        )

    if previous_marks < 60:

        recommendations.append(
            "Focus on improving performance in previous weak subjects."
        )

    if assignment_marks < 60:

        recommendations.append(
            "Complete assignments regularly and improve assignment quality."
        )

    if internal_marks < 60:

        recommendations.append(
            "Prepare better for internal examinations."
        )

    if participation < 5:

        recommendations.append(
            "Participate more actively in classroom activities."
        )

    if not recommendations:

        recommendations.append(
            "Keep up the good work and maintain your current study habits!"
        )

    for recommendation in recommendations:

        st.write("✅", recommendation)


# =========================
# ABOUT PAGE
# =========================

elif page == "ℹ️ About Project":

    st.title("ℹ️ About the Project")

    st.subheader("📌 Project Name")

    st.write(
        "AI-Powered Student Performance Prediction System"
    )

    st.subheader("🧠 Machine Learning Algorithm")

    st.write(
        "Random Forest Regression"
    )

    st.subheader("📥 Input Features")

    st.write(
        """
        • Attendance

        • Study Hours

        • Previous Marks

        • Assignment Marks

        • Internal Marks

        • Class Participation
        """
    )

    st.subheader("📤 Output")

    st.write(
        """
        The system predicts the student's expected final marks
        and provides a performance level and recommendations.
        """
    )

    st.subheader("🛠️ Technologies Used")

    st.write(
        """
        • Python

        • Pandas

        • NumPy

        • Scikit-learn

        • Matplotlib

        • Seaborn

        • Streamlit
        """
    )

    st.divider()

    st.success(
        "🎓 This project demonstrates the use of Machine Learning "
        "for educational performance prediction."
    )                 