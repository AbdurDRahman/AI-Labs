def check(word : str) -> bool:

    special_chars_list = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~' , ' '
    ]
    for character in special_chars_list:
        word = word.replace(character , "") 
    word = word.lower()
    length = len(word)

    for i in range(length):
        if (length - i == i): break

        if(word[i] == word[length-i-1]): continue

        return False
    return True

print(check("Was it a car or a cat I saw"))

    