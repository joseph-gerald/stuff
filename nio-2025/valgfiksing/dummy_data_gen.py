import random

employees_count = 200
employees = []

for i in range(employees_count):
    employees.append([random.randint(0,employees_count-1), random.choice(["G", "S"]), random.randint(2,20)])

employees[0][0] = -1

with open("dummy.txt", "w") as txt:
    txt.write("")

with open("dummy.txt", "a") as txt:
    txt.write(str(employees_count) + "\n")

    for employee in employees:
        if (employee[0] == -1): continue
        txt.write(str(0) + "\n")

    for employee in employees:
        txt.write(employee[1] + " " + str(employee[2]) + "\n")