"1. Write a program to count the number of vowels and consonants present in an input string."
user_input = input("Enter any string:")
abc=list(user_input)

vowels=['a','e','i','o','u']
vow=0
cons=0
print(abc)
for item in abc:
    item=item.lower()
    print(item)
    if item in vowels:
        vow=vow+1
    else:
        cons=cons+1
spa=abc.count(" ")
print(spa)
cons=cons-spa
print("vowels:",vow)
print("Constants:",cons)

