student_name = input("Enter your name: ")
student_score1 = float(input("Enter your score: "))
student_score2 = float(input("Enter your second score: "))
student_score3 = float(input("Enter your third score: "))

average_score = (student_score1 + student_score2 + student_score3) / 3
print(f"{student_name}'s average score is: {round(average_score, 2)}")

if average_score >= 70:
    print(f"Grade: A")
elif average_score >= 60 and average_score < 70:
    print(f"Grade: B")
elif average_score >= 50 and average_score < 60:
    print(f"Grade: C")
elif average_score >= 45 and average_score < 50:
    print(f"Grade: D")
else:
    print(f"Grade: F")




