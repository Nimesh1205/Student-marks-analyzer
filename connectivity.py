import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="HACKATHON2026",
    database="student_marks_analyzer"
)
cursor = conn.cursor()

print("===== STUDENT MARKS ANALYZER =====")
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
print("\nEnter marks out of 100:")
english_marks = int(input("English: "))
hindi_marks = int(input("Hindi: "))
computer_marks = int(input("Computer: "))
science_marks = int(input("Science:"))
socialscience_marks = int(input("Social Science:"))
maths_marks = int(input("Mathematics: "))

marks = [
    english_marks,
    hindi_marks,
    computer_marks,
    science_marks,
    socialscience_marks,
    maths_marks
]

if any(mark < 0 or mark > 100 for mark in marks):
    print("\nInvalid marks! Marks must be between 0 and 100.")

else:
    total_marks = sum(marks)
    maximum_marks = 600
    percentage = (total_marks / maximum_marks) * 100
    cgpa = percentage / 9.5

    query = """
    INSERT INTO students
    (name, roll_no, python_marks, sql_marks, c_marks, maths_marks)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        name,
        roll_no,
        english_marks,
        hindi_marks,
        computer_marks,
        science_marks,
        socialscience_marks,
        maths_marks
    )
    cursor.execute(query, values)
    conn.commit()

    print("\n================================")
    print("       STUDENT RESULT")
    print("================================")

    print("Name       :", name)
    print("Roll No    :", roll_no)

    print("--------------------------------")

    print("English       :", english_marks)
    print("Hindi         :", hindi_marks)
    print("Computer      :", computer_marks)
    print("Science       :", science_marks)
    print("Social Science:", socialscience_marks)
    print("Mathematics   :", maths_marks)

    print("--------------------------------")

    print("Total      :", total_marks, "/", maximum_marks)
    print("Percentage :", round(percentage, 2), "%")
    print("CGPA       :", round(cgpa, 2))

    print("================================")
    print("Data saved successfully!")

cursor.close()
conn.close()