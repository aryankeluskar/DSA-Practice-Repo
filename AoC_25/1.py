# Part 1

# open 1.txt
# with open('AoC_25/1.txt', 'r') as file:
#     lines = file.readlines()

# # print lines
# print(lines)

# list1 = []
# list2 = []

# for line in lines:
#     list1.append(int(line.split("   ")[0]))
#     list2.append(int(line.split("   ")[1]))

# list1 = sorted(list1)
# list2 = sorted(list2)

# # calculate the sum of the absolute differences between the two lists
# sum = 0
# for i in range(len(list1)):
#     sum += abs(list1[i] - list2[i])

# print(sum)

# Part 2

# open 2.txt
with open('AoC_25/1.txt', 'r') as file:
    lines = file.readlines()

# print lines
print(lines)

list1 = []
list2 = []

for line in lines:
    list1.append(int(line.split("   ")[0]))
    list2.append(int(line.split("   ")[1]))

freq = {}

for num in list1:
    freq[num] = 0

for num in list2:
    if num in freq:
        freq[num] += 1

out = 0

for key, value in freq.items():
    out += key * value

print(out)
