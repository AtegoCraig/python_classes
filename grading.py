# Prompt for 8 lab scores
labs = input("Please enter your 8 lab scores separated by commas: ")
labs = [int(score.strip()) for score in labs.split(',')]

if len(labs) != 8:
    print("Error: You must enter exactly 8 lab scores.")
    exit(1)

# Prompt for mid-semester and final exam scores
midsemester = int(input("Please enter your mid-semester exam score: "))
final = int(input("Please enter your final exam score: "))

# Normalize lab scores to 100
labs_average = sum(labs) / 8
labs_normalized = (labs_average / 20) * 100
labs_weighted = labs_normalized * 0.5

# Exams are assumed to be out of 100
exams_weighted = ((midsemester + final) / 2) * 0.5

# Calculate final grade
final_grade = labs_weighted + exams_weighted

if final_grade >= 90:
    letter_grade = 'A'
elif final_grade >= 80:
    letter_grade = 'B'
elif final_grade >= 70:
    letter_grade = 'C'
elif final_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Output the final grade and letter grade
print(f"Your grade is {letter_grade} with a final score of {final_grade:.2f}.")