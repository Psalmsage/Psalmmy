f = open("story 1.txt", "r")
read_data = f.read()
per_word = read_data.split()
print(read_data)
  
print('Total words:',len(per_word))
search_word_count=input("Enter the word to search:")
f=open("story 1.txt", "r")
read_data= f.read()
word_count=read_data.lower().count(search_word_count)
print(f"The word'{search_word_count}' appeared {word_count}times.")