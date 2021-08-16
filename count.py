intro=input("enter your message:")
character_count=0
word_count=1
for character in intro:
    character_count=character_count+1
    if(character==" "):
        word_count=word_count+1
print("number of character")
print(character_count)
print("number of words")
print(word_count)