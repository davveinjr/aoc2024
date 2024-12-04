def check_safety(report):
    safety_score = 0
    if len(report) != len(set(report)):
        safety_score -= abs(len(report) - len(set(report)))
    
    for i in range(len(report)):
        direction = ''
        if i == len(report) - 1:
            if safety_score == 0:
                safety_score += 1
        else:
            if report[i] > report[i+1]:
                direction = 'Decreasing'
            else: 
                direction = 'Increasing'

            
            if abs(report[i] - report[i+1]) > 3:
                safety_score -= 1

    return safety_score

safe = 0
unsafe = 0

with open('input.txt', 'r') as file:
    for line in file:
        report = [int(x) for x in line.split()]
        for i in range(len(report)):
            if report == sorted(report) or report == sorted(report, reverse = True):
                if i == len(report) - 1:
                    if len(report) == len(set(report)):
                        safe += 1
                    else: 
                        unsafe += 1
                else:
                    if abs(report[i] - report[i+1]) > 3:
                        unsafe += 1
                        break
            else:
                unsafe += 1
                break

safe_p2 = 0

with open('input.txt', 'r') as file:
    for line in file:
        report = [int(x) for x in line.split()]
        score = check_safety(report)
        if score <= -1:
            safe_p2 += 1

print("Part 1: ", safe)
print("Part 2: ", safe_p2)
