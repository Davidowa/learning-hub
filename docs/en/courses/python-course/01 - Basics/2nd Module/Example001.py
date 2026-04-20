# Let's do a program that prints the even number from 1 to 10
# And also count the number of even numbers

count = 0
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")
