a=input("enter any word")
b=input("enter any word")
a=a.lower()
b=b.lower()
if(len(a)==len(b)):
    sorted_a=sorted(a)
    sorted_b=sorted(b)
 
    if(sorted_a==sorted_b):
       print(a + "and" + b + "are anagrams.")
    else:
         print(a + "and" + b + "are not anagrams.")
