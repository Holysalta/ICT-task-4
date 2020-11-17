postal_code = {
    'Newfoundland':'A',
    'Nova Scotia':'B',
    'Prince Edward Island':'C',
    'New Brunswick':'E',
    'Quebec':['G','H','J'],
    'Ontario':['K','L','M','N','P'],
    'Manitoba':'R',
    'Saskatchewan':'S',
    'Alberta':'T',
    'British Columbia': 'V',
    'Nunavut':'X',
    'Northwest Territories':'X',
    'Yukon':'Y'
}

def reverse_lookup(find_dict, value):
    output = []
    for key in find_dict:
        if(isinstance(find_dict[key],list)):
            for i in range(len(find_dict[key])):
                if(find_dict[key][i] == value):
                    output.append(key)        
        else:
            if(find_dict[key] == value):
                output.append(key)
    return output

text = input("Write code: ")

location = reverse_lookup(postal_code, text[0])
output = ""
if(len(location)==0):
    print("No valid postal code")
elif(len(location)==1):
    if(int(text[1])>0):
        output += "urban address "
        output += "in " + location[0]
    else:
        output += "rural address "
        output += "in " + location[0]
else:
    if(int(text[1])>0):
        output += "urban address "
        output += "in " + location[0]
    else:
        output += "rural address "
        output += "in " + location[0] + " or " + location[1]
print(output)