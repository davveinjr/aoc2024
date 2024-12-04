import re

def mul(mem):
    nums = re.findall(r"\d+", mem)
    return (int(nums[0]) * int(nums[1]))

def mul_p2(mem):
    execute = True
    line_total = 0

    for inst in mem:
        if inst == "don't()": 
            execute = False
        elif inst == "do()":
            execute = True
        else:
            if(execute):
                nums = re.findall(r"\d+", inst)
                line_total += (int(nums[0]) * int(nums[1]))
    return line_total

p1_total = 0
p2_total = 0

with open("input.txt", "r") as file: 
    for line in file: 
        instructions = re.findall(r"mul\(\d+,\d+\)", line)
        instructions_p2 = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line) 

        p2_total += mul_p2(instructions_p2)
        for item in instructions:
            p1_total += mul(item)


print("Part 1: ", p1_total)
print("Part 2: ", p2_total)
