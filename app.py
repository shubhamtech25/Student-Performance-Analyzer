import streamlit as st
import pandas as pd

st.title("Student Performance Analyzer")

st.write("Analyze student academic performance.")

name = st.text_input("Enter Student Name")
roll = st.text_input("Enter Roll Number")

subjects = ["Python", "Mathematics", "DBMS", "Java", "DSA"]

marks = []

for subject in subjects:
    mark = st.number_input(
        f"Enter {subject} Marks",
        min_value=0,
        max_value=100,
        value=0
    )
    marks.append(mark)

if st.button("Analyze Performance"):

    if name.strip() and roll.strip():

        total = sum(marks)
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        st.success(f"Student Name: {name}")
        st.write("Roll Number:", roll)
        st.write("Total Marks:", total, "/ 500")
        st.write("Percentage:", percentage, "%")
        st.write("Grade:", grade)

        df = pd.DataFrame({
            "Subject": subjects,
            "Marks": marks
        })

        st.bar_chart(df.set_index("Subject"))

    else:
        st.warning("Please enter student details.")