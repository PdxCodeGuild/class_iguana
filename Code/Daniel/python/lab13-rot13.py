
rot13 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

sentence = input('Enter a string: ')
encoded = []

if sentence.isalpha():
    for i in sentence:
        letter_index = rot13.index(i)
        # letter_index = (letter_index + 13)%26
        if letter_index > 12:
            encoded.append(rot13[letter_index + 13 - 26])
        else:
            encoded.append(rot13[letter_index + 13])

    print('Encoded string: ' + ''.join(encoded))

else:
    print('Not a valid string')




