#making rot13 function attached to dictionary
def rot13(user_string):
    rot_dict = {'a': 'n',
                'b': 'o',
                'c': 'p',
                'd': 'q',
                'e': 'r',
                'f': 's',
                'g': 't',
                'h': 'u',
                'i': 'v',
                'j': 'w',
                'k': 'x',
                'l': 'y',
                'm': 'z',
                'n': 'a',
                'o': 'b',
                'p': 'c',
                'q': 'd',
                'r': 'e',
                's': 'f',
                't': 'g',
                'u': 'h',
                'v': 'i',
                'w': 'j',
                'x': 'k',
                'y': 'z'}
#blank string output
    output = ''
    for char in user_string:
        print(f'{char} {rot_dict[char]}')
#for loop; each character in input string used as key in dictionary to encode input string with dictionary
user_string = input('please help me generate a string: ')
print(rot13(user_string))
#print function and user string