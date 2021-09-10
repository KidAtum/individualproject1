#Lucas Weakland
#Algorithms Analysis
#Individual Project 1

#Standard interval
#non user input path dunno which to use
num_strings = ["13", "5", "9", "99", "64", "3"]

num_strings.sort(key=int)

print(num_strings)
#user input path
str_input = input("Please enter numbers separated by spaces: ")

# split the string into numbers & create a list of numbers
numbers = [int(x) for x in str_input.split()]

count = len(numbers)

for outer in range(count - 1):  # bubbles each number to the end
    for i in range(count - outer - 1):
        if numbers[i] > numbers[i + 1]:
            # swap numbers algorithm
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#print the sorted numbers
print(numbers)

#Weighted interval
print("Now please insert a weighted interval schedule (example: [a, 2], [b, 1], [c, 0]")#user input not working yet

multi_list = [["a", 2], ["b", 1], ["c", 0]]

sorted_multi_list = sorted(multi_list, key=lambda x: x[1])

print(sorted_multi_list)