📌 Project Title

>Student Eligibility Checker Using Python

📖 Description

>This Python program checks whether a student is eligible based on two criteria:
>Marks must be 40 or above.
>Attendance must be 75% or above.
>If both conditions are satisfied, the student is declared Eligible. Otherwise, the program displays Not Eligible.

🚀 Features
>Accepts marks as input.
>Accepts attendance percentage as input.
>Uses conditional statements (if, elif, else).
>Demonstrates logical operators (and, or).
>Beginner-friendly project.
🛠️ Technologies Used
>Python 3
💻 Code:Python
>marks = float(input("Enter marks out of 100: "))
>att = float(input("Enter attendance in percentage: "))
>
>if marks >= 40 and att >= 75:
>print("Eligible")
>elif marks >= 40 or att >= 75:
>print("Not Eligible")
>else:
>print("Not Eligible")
 
▶️ How to Run
>Install Python 3 on your computer.
>Save the code as eligibility_checker.py.
>Open the terminal or command prompt.
>Navigate to the project folder.
Run:
>Shell
>python eligibility_checker.py
📷 Example Output:
Example 1:
>Plain Text
>Enter marks out of 100: 65
>Enter attendance in percentage: 80
>Eligible
Example 2:
>Plain Text
>Enter marks out of 100: 55
>Enter attendance in percentage: 60
>Not Eligible
>Example 3
>Plain Text
>Enter marks out of 100: 30
>Enter attendance in percentage: 80
>Not Eligible
📚 Concepts Learned
>Taking user input
>Converting data using float()
>Conditional statements (if, elif, else)
>Logical operators (and, or)
>Decision-making in Python
🔮 Future Improvements:
>Add grade calculation.
>Validate marks and attendance ranges.
>Display reasons for ineligibility.
Store student records in a file.
A beginner Python project created to practice conditional statements and logical operators. Ideal for students learning basic decision-making programs in Python.
