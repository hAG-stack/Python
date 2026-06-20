students = [{"name": "Ahmed", "grades":[80,75,65]},{"name": "Mohamed", "grades":[90,85,70]},{"name": "Yassin", "grades":[70,80,85]}]
for student in students :
    average = sum(student["grades"]) / len(student["grades"])
    print( student["name"] , "Average grade : ", average)