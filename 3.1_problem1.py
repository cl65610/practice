import string
input_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1,
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}
lower_vowels = ['a', 'e', 'i', 'o', 'u']
def dictionary(dict):
    print dict
    for i in dict.keys():
        t = str(i)
        if t[0] in lower_vowels:
            dict[i] = 'vowel'
        elif t[0] in string.ascii_lowercase:
            dict[i] = 'consonant'
        else:
            del dict[i]
    print dict
    return dict
dictionary(input_dict)
