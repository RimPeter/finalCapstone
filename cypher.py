# provide text to test
text = 'abcdefghijklmnopqrstuvwxyz%ABCDEFGHIJKLMNOPQRSTUVWXYZ,./;'
# create function
def codon(text):
    #variable for new text
    newtext = ""

    # iterate through text
    for i in range(len(text)):
        letter = text[i]

        # code uppercase letters
        if (letter.isupper()):
            '''upper case letters are numbered from 65 to 90,
            and because we have to cycle around anything over 75 has 
            to be deducted by 11 instead of adding 15.'''
            if ord(letter) <= 75:
                newtext += chr(ord(letter)+15)
            elif ord(letter) >75:
                newtext += chr(ord(letter)-11)

        # code lowercase letters
        elif (letter.islower()):
            '''lower case letters are numbered from 97 to 122,
            and because we have to cycle around anything over 107 has 
            to be deducted by 11 instead of adding 15.'''
            if ord(letter) <= 107:
                # ord(letter) means: letter turns into an ASCII value
                # ord(letter)+15 means: we add 15 to that value, so we get a different value
                # chr(ord(letter)+15) means: we turn that different value back to a different letter
                newtext += chr(ord(letter)+15)
            elif ord(letter) >107:
                newtext += chr(ord(letter)-11)

        # everything else stays unchanged
        else:
            newtext += letter
    #return new text as one single string
    return newtext

# provide text and print it and also print it with codon function
print("Text: " + text)
print("Coded Text: " + codon(text))


# create function
def codoff(text):
    # variable for new text
    newtext = ""

    # iterate through text
    for i in range(len(text)):
        letter = text[i]

        # decode uppercase letters
        if (letter.isupper()):
            if ord(letter) >= 80:
                newtext += chr(ord(letter)-15)
            elif ord(letter) <80:
                newtext += chr(ord(letter)+11)

        # decode lowercase letters
        elif (letter.islower()):
            if ord(letter) >= 112:
                newtext += chr(ord(letter)-15)
            elif ord(letter) <112:
                newtext += chr(ord(letter)+11)

        # everything else stays unchanged
        else:
            newtext += letter
    # return new text as one single string
    return newtext

# provide coded text and print it and also print it with codoff function
coded_text = "pqrstuvwxyzabcdefghijklmno%PQRSTUVWXYZABCDEFGHIJKLMNO,./;"
print("Coded Text: " + coded_text)
print("Decoded Text: " + codoff(coded_text))
