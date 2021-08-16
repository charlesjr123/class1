def count():
    file_name=input("please enter name")
    f=open(file_name,"r")
    word_count=0
    for line in f:
        word=line.split()
        word_count=word_count+len(word)
    
    print("number of words")
    print(word_count)

count()