#Find_anagrams("hello","check")
False
#Find_anagrams("below","elbow")
True
 
a=(input("enter any word"))
b=(input("enter any word"))
#make all word small letter/Case to check properly
a=a.lower()
b=b.lower()
#check if lenght is same
if(len(a)==len(b)):
    sorted_a = sorted(a)
    sorted_b=sorted(b)

    if (sorted_a==sorted_b):
        print(a + "and" + b + "are anagrams.")
    else:
        print(a + "and" + b + "are not anagrams.")