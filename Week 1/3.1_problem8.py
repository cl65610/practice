first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}

def string_inlist_cleaner(dict):
    for item in dict.keys():
        if type(item) is not str:
            del dict[item]
        elif type(dict[item]) is not list:
            del dict[item]
    return dict

def int_string_cleaner(dict):
    for item in dict.keys():
        if type(item) is not int:
            del dict[item]
        elif type(dict[item]) is not str:
            del dict[item]
    return dict

def dict_cleaner(dict1, dict2):
    print 'Dictionary 1: ', dict1
    print 'Dictionary 2: ', dict2
    cleaned = {}
    dict1_clean = string_inlist_cleaner(dict1)
    dict2_clean = int_string_cleaner(dict2)
    for item in dict1_clean:
        cleaned[item] = dict1_clean[item]
    for item in dict2_clean:
        cleaned[item] = dict2_clean[item]
    print cleaned
    return cleaned

dict_cleaner(first_dict, second_dict)
