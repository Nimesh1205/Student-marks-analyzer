import numpy as np
import pandas as pd
from ollama import chat

# Reading csv data
student_marks_df=pd.read_csv("data/student_marks.csv")
student_marks_df=student_marks_df.set_index("Roll_No")
student_marks_df

def student_info(roll_no):
    return student_marks_df.loc[roll_no]

def subject_data(roll_no):
    return student_marks_df.loc[roll_no,"Maths":"Civics"]

def student_analyzer(roll_no):
    student = student_marks_df.loc[roll_no]
    marks = student["Maths":"Civics"]

    total = marks.sum()
    average = marks.mean()

    strong_subjects = marks[marks >= 75]
    weak_subjects = marks[marks < 50]

    highest_subject = marks.idxmax()
    highest_mark = marks.max()

    lowest_subject = marks.idxmin()
    lowest_mark = marks.min()

    print(f"""
Marksheet
-------------------------------------------------------
Name:{student["Name"]}
dob:{student["DOB"]}
-------------------------------------------------------
Total marks: {total}/800
Total percentage: {average:.2f}%
-------------------------------------------------------
Strongest subject(s):
{strong_subjects.to_string()}
-------------------------------------------------------
Weakest subject(s):
{weak_subjects.to_string()}
-------------------------------------------------------
Highest subject:
{highest_subject}: {highest_mark}

Lowest subject:
{lowest_subject}: {lowest_mark}
-------------------------------------------------------
""")

    prompt=f"""
Analyze This student's academic performance
Name:{student["Name"]}
dob:{student["DOB"]}
Total marks: {total}/800
Total percentage: {average:.2f}%
Strongest subject(s):
{strong_subjects}
Weakest subject(s):
{weak_subjects}
Highest subject(s):
{highest_subject}
{highest_mark}
Lowest subject(s):
{lowest_subject}
{lowest_mark}

Give the analysis with clear headings and bullet points:
1.Area needing improvement
2.Overall Performance
3.Study Recommendations
"""
    return prompt

roll_no=int(input("Enter Student's Roll No: \n"))
prompt=student_analyzer(roll_no)
response = chat(
    model="qwen2.5-coder:3b",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ]
)

print(response["message"]["content"])