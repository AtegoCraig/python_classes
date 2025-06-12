# Sum of the first N natural numbers using a while loop

N = int(input("Enter a positive integer N: "))
total = 0
i = 1

while i <= N:
    total += i
    i += 1

print(f"The sum of the first {N} natural numbers is {total}.")