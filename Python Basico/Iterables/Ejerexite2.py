def verify_positives(list):
    count_negatives= 0
    for num in list:
        if num <= 0:
            count_negatives += 1
    if count_negatives == 0:
        return True
    else: 
        return count_negatives
list= [25, 45, -5, 60, 1]
result= verify_positives(list)
if result is True:
        print("All numbers are positives")
else:
        print(f"There is at list one negative number. Count of negative numbers {result}")