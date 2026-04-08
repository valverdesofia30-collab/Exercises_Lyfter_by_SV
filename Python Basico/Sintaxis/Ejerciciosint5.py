n = int(input("How many grades do you want to enter?"))
total_sum = 0
approve_sum = 0
approve_counter = 0
disapproved_sum = 0
disapproved_counter = 0
approve_average = 0
disapproved_average = 0
for i in range(n):
    grade = float(input(f"Enter the grade {i+1}"))
    total_sum += grade
    if grade > 70:
        approve_sum += grade
        approve_counter += 1
    elif grade < 70:
        disapproved_sum += grade
        disapproved_counter += 1
    total_average: float = total_sum / n
    if approve_counter > 0:
            approve_average = approve_sum / approve_counter
            approve_average = 0
            if disapproved_counter > 0:
                disapproved_average = disapproved_sum / disapproved_counter
            else:
                disapproved_average = 0
print("Approve grades:", approve_counter)
print("Disapproved grades:", disapproved_counter)
print("Total average:", total_average)
print("Approve average:", approve_average)
print("Disapprove average:", disapproved_average)