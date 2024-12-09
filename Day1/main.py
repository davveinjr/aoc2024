l = []
r = []
diff = 0 
similarity = 0



with open('input.txt', 'r') as file:
    for line in file:
        nums = line.split(" "*line.count(" "))
        l.append(int(nums[0]))
        r.append(int(nums[1]))

l.sort()
r.sort()

for index in range(len(l)):
    diff += abs(int(l[index]) - int(r[index]))   

for num in l:
    matches = [x for x in r if x == num]
    similarity += (num * len(matches))

print("Part 0: ", diff)
print("Part 1: ", similarity)
