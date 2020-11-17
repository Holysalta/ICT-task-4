num2words1 = {0:"",1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = {20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}

num2words3 = {100 : 'One hundred', 200 : 'Two hundred', 300 : 'Three hundred', 400 : 'Four hundred', 500 : 'Five hundred', 600:'Six hundred', 700:'Seven hundred', 800:'Eight hundred', 900:'Nine hundred'}



def number(Number):
    if (Number >= 0) and (Number <= 19):
        return (num2words1[Number])
    elif (Number >= 20) and (Number <= 99):
        return (num2words2[Number])
    elif (Number >= 100) and (Number <= 1000):
        return (num2words3[Number])

num = int(input("Enter some number"))
num1 = int(num / 100)
num2 = num % 10 - num % 10
num3 = num % 10
output = ""

print(num1)
print(num2)
print(num3)
if(num1 > 0):
    output+= number(num1*100)
    output+=" "
if(num2 > 0):
    output+= number(num2*10)
    output+= " "
if(num3 > 0):
    output+= number(num3)
output