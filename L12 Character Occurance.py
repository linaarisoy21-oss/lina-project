#Take input of a word
string = input("Please enter your own word or sentence : ")

#take input of character which the user entered
char = input("Please enter your own Character : ")

i = 0
count = 0

#loop will find the occurence of character
while(i < len(string)): #string operation
    if(string[i] == char): #check each letter of the word wether it's the sane as the character we want to find
        count = count + 1

    i = i + 1 #increase the i value until the length of the word. i is the position of each letter in the word

#Display the result
print(f"The total Number {char} character has occurred = {count} times")