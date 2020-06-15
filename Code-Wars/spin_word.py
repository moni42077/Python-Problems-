# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(sentence):
    converted = ""
    for i in sentence.split():
        if len(i) >= 5:
            converted += ''.join(reversed(i))
            converted += ' '
        else:
            converted += i
            converted += ' '
    converted = converted[:-1]  # removing the space after the last letter
    return(converted)


print(spin_words('Hey fellow warriors'))

# can be done in one line as   return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
