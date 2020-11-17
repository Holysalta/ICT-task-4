def anagram_again(text1, text2):
    text1 = text1.replace(" ", "")
    text2 = text2.replace(" ", "")
    text1 = text1.lower()
    text2 = text2.lower()
    text1_dict = {}
    text2_dict = {}
    if(len(text1) != len(text2)):
        return False
    for i in range(len(text1)):
        text1_dict[text1[i]] = 0
        text2_dict[text2[i]] = 0
    for i in range(len(text1)):
        text1_dict[text1[i]] += 1
        text2_dict[text2[i]] += 1
    flag = True
    for i in range(len(text1)):
        if((not(text1[i] in text2_dict.keys())) or text1_dict[text1[i]] != text2_dict[text1[i]]):
            flag = False
            break
    print(flag)
anagram_again("William Shakespeare", "I am a weakish speller")