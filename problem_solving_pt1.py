#get the word
#user_word = input("What word would you like to reverse? ")

#how do you get the last letter?
#last_letter = user_word[-1]
#find the length of the word
#lenght_of_word = len(user_word)
#how do we iterate over the string to get the value for each index
"for index in range():"


#how does range work?
"range(start, stop, increment_by)"

#with the info we gathered so far, how can we fit it together to iterate over the string, starting from the last index to the first, printing each value at index?

# for index in user_word.range(user_word[-1],len(user_word), -1):
#     "print(user_word[-1])

#we know we want to print the value at the current index to starting with the last which is at -1 but how do we loop properly?
# for index in range(0, len(user_word) - 1):
#         print(index)

#through trial and error, we came up with a way to use the length of the word to count backwards... but now we need to print the values of the index, not the index
#for index in range(len(user_word) -1, -1,-1):
    #print(index[-1]) #did not work probably beause im calling the index of an index

# for index in range(len(user_word) -1, -1,-1):
#     print(user_word[index]) 


# its working, not i need to try a print it in a single line but adding it together
# reversed_word = ""
# for index in range(len(user_word) -1, -1,-1):
#     reversed_word += user_word[index]
#
#      print(reversed_word) it worked but didnt print like we wanted, maybe we could try combining every thing in a function


def reverse_word():
    user_word = input("What word would you like to reverse? ")
    reversed_user_word = ""
    for index in range(len(user_word) -1, -1, -1):
        reversed_user_word += user_word[index]
    return reversed_user_word


print(reverse_word())