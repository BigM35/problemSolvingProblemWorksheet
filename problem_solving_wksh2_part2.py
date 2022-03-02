#Prime numbers

#formular for prime numbers 6(n) - 1 = Prime and 6(n) + 1 = prime for 1-40, pass 40, the formula will be n2+n+41

#first, make a for loop with range 0 - 100
#fist numbers to be display should be  2, 3.
print("2\n3")
for number in range(1,7):
    prime = 6 * number - 1
    if prime == 35:
        pass
    else:
        print(prime)
    prime = 6 * number + 1
    if prime == 25:
        continue
    else:
        print(prime)
for number in range(0,8):
    prime = number ** 2 + number + 41
    print(prime)


# for number in range(1,7):
#     if number % 2 == 0:
#        prime = 3 * number - 1
#        print(prime)
#     if number % 2 == 1:
#         prime = 3 * number - 10
#         print(prime)
#     elif number == 2 or number == 12:
#         prime = 3 * number + 1
#         print(prime)
#     elif number == 5:
#         prime = 3 * number - 2
#         print(prime)
#     elif number == 5:
#         prime = 3 * number + 2
#         print(prime)
#     elif number == 0 or 10:
#         prime = 3 * number - 2
#         print(prime)
#     elif number == 0 or 10:
#         prime = 3 * number + 2
#         print(prime)
