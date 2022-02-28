#Capitalization
#how do make the first letter in a string upper case
#     -.toUpperCase() function
# how do you cut a string up to a series of single word?
#     -.slice methoid 


# def capitalize_a_letter():
#     user_input = input("Enter a sentence, the first letter of each word will be capitalize for you!: ")
#     sliced_input = user_input.split(" ")
#     print(sliced_input) # typed in "Hello, my name is Manny and i am working hard to be a successful software developer!" 
#                         #returned ['Hello,', 'im', 'name', 'is', 'Manny', 'and', 'i', 'am', 'working', 'hard', 'to', 'be', 'a', 'successful', 'software', 'developer!']
#     joined_input = " ".join(sliced_input)
#     print(joined_input) #returned 

# capitalize_a_letter()

# now we know how to split and join, we can make a function the split the sentence into a list, iterate over it, use the .capitialize()function to capitalize each word and append it into a list of capitalize first letter. Then return the value joined.
def capitalize_first_letter_of_each_word():
    user_input = input("Enter a sentence, the first letter of each word will be capitalize for you!: ")
    split_input = user_input.split(" ")
    capitalize_list = []
    for index in range(0,len(split_input)):
        cap_word = split_input[index].capitalize()
        capitalize_list.append(cap_word)
    return " ".join(capitalize_list)

print(capitalize_first_letter_of_each_word())
