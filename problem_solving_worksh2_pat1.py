# Happy numbers
#First find a way to break a given number into digits
    #       -convert int into str
    #       -iterate over number string
    #       -append int result into a list
    #       
# using a while loop, square each digits
    #       -iterate over the list of int and square the value
#check if digits are equal to 1
#if not, repeat
#how do i break out the loop?

#output = "0"

# squared_digits = [int(num) ** 2 for num in str(user_input)]
# for num in range(len(squared_digits)):
#     output += str(squared_digits[num])
#     converet_to_int = int(output)
# while True:
#     inner_output = "0"
#     if converet_to_int > 1:
#         new_squared_digi = [int(num) ** 2 for num in str(converet_to_int)]
#         for index in range(len(new_squared_digi)):
#             sums = 0
#             sums += (new_squared_digi[index])
#             converet_to_int = sums
#         if user_input == converet_to_int:
#             print(f"{user_input} is an unhappy number!")
#             break
#         elif converet_to_int == 1:
#             print(f"{user_input} is a happy number!")
user_input = int(input("Enter a set of numbers to find out if it is a happy number or not: "))
def happy_number_finder():
    
    new_user_input = user_input
    while True:
        if new_user_input > 1:
            new_user_input = str(new_user_input)
            sum_of_squared_nums = 0
            for char in new_user_input:
                char_int = int(char)
                char_squared = char_int * char_int
                sum_of_squared_nums += char_squared
                new_user_input = sum_of_squared_nums
            if new_user_input == 1:
                print(f"{user_input} is a happy number!")
                break
            elif new_user_input == 4:
                print(f"{user_input} is an unhappy number!")
                break
        else:
            print(f"{user_input} is an unhappy number!")
            break
            
            
print(happy_number_finder())