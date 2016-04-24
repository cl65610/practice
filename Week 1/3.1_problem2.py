def remainders(dict, remainder=[]):
    if len(remainder) == 0:
        remainder.append(2)
    print dict
    print remainder
    new_remainders= {}
    for item in dict:
           for n in dict[item]:
                new_remainders[n] = [n%r for r in remainder]
                dict[item] = [n%r for r in remainder]
    print new_remainders
    print dict
    return new_remainders
test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
optional_remainder = [2,3,4,5]
remainders(test_dict, optional_remainder)
