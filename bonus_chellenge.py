#Palindrome

#Check user input

#determine how to find the middle character in a given word

#iterate over the user word

#determine if the first and last letter are equal...

#repeat until you get to the letter before the mid letter

# if it gets to the middle letter its Palindrome.

def check_palindrome():
    user_input = "level"
    front_val = ""
    back_val = ""
    if len(user_input) % 2 == 1:
        mid_index = int(len(user_input) / 2)
        for character in range(0,mid_index):
            front_val += user_input[character]
        for char in range(len(user_input) - 1, not mid_index, -1):
            back_val = user_input[char]
            if front_val in back_val:
                print(f"{user_input} is a Palindrome!")
                    
    
    else:
        print (f"{user_input} is not a Palindrome!")

check_palindrome()