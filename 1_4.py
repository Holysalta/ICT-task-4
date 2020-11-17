def reverse_lookup(find_dict, value):
    output = []
    for key in find_dict:
        if(find_dict[key] == value):
            output.append(key)
    return output

some_dict = {"one": 1, "two": 2, "odin": 1, "six": 6, "seven": 7, "eleven": 11, "three" : 3}

print(reverse_lookup(some_dict, 1))
print(reverse_lookup(some_dict, 6))
print(reverse_lookup(some_dict, 10))