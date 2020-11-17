def count_unique_character(text):
    unique_characters = []
    for i in range(len(text)):
        if(not(text[i] in unique_characters)):
            unique_characters.append(text[i])
    print(len(unique_characters))
text = input("some text: ")
count_unique_character(text)
