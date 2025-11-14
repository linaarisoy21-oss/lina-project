#input a word
text = input("Enter a string: ")

# Reverse String
# using step value as -1 to iterate in reverse
revtext = text[::-1]
text = revtext

print ("Reverse of given string is:")
print(text)

print()

#convert to uppercase
message = "python is fun"
upper = message.upper()
print(upper)