
textLetters = {
'1':['.',',','?','!',':'],
'2':['A','B','C'],
'3':['D','E','F'],
'4':['G','H','I'],
'5':['J','K','L'],
'6':['M','N','O'],
'7':['P','Q','R','S'],
'8':['T','U','V'],
'9':['W','X','Y','Z'],
'0':[' ']
}

text = input()
new_output = ""
def countt(text):
    count = 0
    index = 0
    for i in range(len(text)):
        count += 1
        if(len(text) - i == 1 or text[0] != text[i+1]):
            index = i + 1
            break
    return count - 1, index, text[index-1]
while(text != ""):
    output, next_elem, num = countt(text)
    text = text[next_elem:]
    if(num=='7' or num=='9' or num=='1'):
        new_output += textLetters[num][output%4]
    else:
        new_output += textLetters[num][output%3]
new_output