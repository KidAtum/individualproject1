#Lucas Weakland
#Algorithms Analysis
#Individual Project 1
#SIDE NOTE : I have been reading and watching hours of algorithm based things in all languages. I really am trying
# for this class,this is a super cool topic to learn. I just hope I am doing it right. If you have any pointers or
# anything please let me know. I actually really do care about this stuff and want to get better with it.

#Standard interval
#non user input path
numString = ["13", "5", "9", "99", "64", "3"]
numString.sort(key=int)
print(numString)

#user input path
stringInput = input("Please enter numbers separated by spaces (user input version for standard interval): ")

# make string into numbers and create a list of numbers
numbers = [int(x) for x in stringInput.split()]
count = len(numbers)
for outer in range(count - 1):
    for i in range(count - outer - 1):
        if numbers[i] > numbers[i + 1]:
            # swap numbers algorithm
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#print the sorted numbers
print(numbers)

#Weighted interval test code
print("This is the test version of the weighted interval scheduling..")#decided to keep this in here cuz why not
multiList = [["a", 2], ["b", 1], ["c", 0]]
sortedMultiList = sorted(multiList, key=lambda x: x[1])
print(sortedMultiList)

#real weighted interval schedule
# class for job
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

# this function will find the latest job that doesnt conflict with the current job
def binarySearch(job, start_index):
    lo = 0
    hi = start_index - 1
    # Type of binary search (seems to be efficient even tho were not fully focusing on that yet
    while lo <= hi:
        mid = (lo + hi) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1
# function that shows/returns the most possibility of profit
def schedule(job) -> object:
    # sort the jobs with consideration to finish time
    job = sorted(job, key=lambda j: j.finish)
    # creates array to store profitable jobs
    n = len(job)
    table = [0 for _ in range(n)]
    table[0] = job[0].profit;
    for i in range(1, n):
        # find the profit in the current job
        inclProf = job[i].profit
        l = binarySearch(job, i)
        if (l != -1):
            inclProf += table[l];
        table[i] = max(inclProf, table[i - 1])
    return table[n - 1]
# heres the code that i used to test this whole algorithm or whatever
job = [Job(1, 2, 50), Job(3, 5, 20),
       Job(6, 19, 100), Job(2, 100, 200)]
print("Optimal profit is"),
print(schedule(job))
# i hope this is what you wanted. I really do not know. sorry if its not, I will fix whatever you need to be fixed
# hope your having a good night (your reading this at 2;33am)