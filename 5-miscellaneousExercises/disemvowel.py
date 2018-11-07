# OK, I need you to finish writing a function for me. The function disemvowel takes 
# a single word as a parameter and then returns that word at the end.

# I need you to make it so, inside of the function, all of the vowels
#  ("a", "e", "i", "o", and "u") are removed from the word. Solve this however you want, 
# it's totally up to you!

# Oh, be sure to look for both uppercase and lowercase vowels!

def disemvowel(word):
    vowels = "aeiouAEIOU"
    new_word = []

    for letter in word:
        if letter not in vowels:
            new_word.append(letter)

    new_word = ''.join(new_word)
    return new_word

print(disemvowel('Aerianeeeeeeeeeeeeeee'))