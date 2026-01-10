
starting = input("Enter the starting number: ")
ending = input("Enter the ending number: ")

perfect_numbers = []

for num in range(int(starting), int(ending) + 1):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == num:
        perfect_numbers.append(num)

print("Perfect numbers between", starting, "and", ending, "are:", perfect_numbers)

