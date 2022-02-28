
#Compress strings
random_char = "aaabbbbbccccaacccbbbaaabbbaaa"

#first, iterate over the string
#then use the count function to count each character
#concatinate or string interpolate the count and the character...
#a
def count_letters():
    letters_and_counts = ""
    for char in random_char:
        if char not in letters_and_counts:
            count = random_char.count(char)
            letters_and_counts += f"{count}{char}"
        else:
            continue
    return letters_and_counts
print(count_letters())



