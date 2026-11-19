#1 Initialize
grade = 0
letterGrade = ""
passed = 1
#2 Get Data
grade = int(input("what is the grade"))
#3 Do the work
if grade >= 90:
 if grade >= 93:
   letterGrade = "A"
 else:
     letterGrade = "A-"
elif grade >= 80: 
    letterGrade = "B"
    if grade < 83:
        letterGrade += "-"
    elif grade > 86:
        letterGrade += "+"
elif grade >= 70:
      letterGrade ="C"
      if grade < 73:
       letterGrade += "-"
elif grade > 76:
    letterGrade += "+"
elif grade >= 60:
    letterGrade ="D"
    if grade < 63:
     letterGrade += "-"
    elif grade > 66:
     letterGrade += "+"
    passed = 0
elif grade <= 60:
    letterGrade = "F" 
    passed = 0
#4 Display results
print (f"Your grade is a {letterGrade}")
if passed:
     print("Congratulations you passed the course!")
else:

    print("Sorry you did not pass the course :<")



