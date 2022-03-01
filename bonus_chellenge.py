#Palindrome

#Check user input

#determine how to find the middle character in a given word

#iterate over the user word

#determine if the first and last letter are equal...

#repeat until you get to the letter before the mid letter

# if it gets to the middle letter its Palindrome.

def check_palindrome():
    user_input = input("Enter a word to to check if its a palindrome or not: ")
    front_val = ""
    back_val = ""
    if len(user_input) % 2 == 1:
        mid_index = int(len(user_input) / 2)
        for character in range(0,mid_index):
            front_val += user_input[character]
        for char in user_input[:- mid_index - 1: - 1]:
            back_val += char
        if front_val == back_val:
            print(f"{user_input} is a Palindrome!")
        else:
            print (f"{user_input} is not a Palindrome!")            
    else:
        mid_index = int(len(user_input) / 2) + 1
        for character in range(0,mid_index):
            front_val += user_input[character]
        for char in user_input[:- mid_index - 1: - 1]:
            back_val += char
        if front_val == back_val:
            print(f"{user_input} is a Palindrome!")
        else:
            print (f"{user_input} is not a Palindrome!")
       
check_palindrome()
