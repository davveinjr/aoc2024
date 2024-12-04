l = []
r = []
diff = 0
similarity = 0

with open('input.txt', 'r') as file:
    for line in file:
        nums = line.split(" "*line.count(" "))
        l.append(nums[0])
        r.append(nums[1])

l.sort()
r.sort()

for index in range(len(l)):
    diff += abs(int(l[index]) - int(r[index]))   

for num in l:
    matches = [x for x in r if str(x) == str(num)]
    similarity += (int(num) * len(matches))
    
print(type(l), type(l[1]))
print(type(r), type(r[1]))

print("Part 1: ", diff)
print("Part 2: ", similarity)
