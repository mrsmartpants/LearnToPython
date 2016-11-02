
# A-Z 65-90
# a-z 97-122

stringentered = input("Enter a string in uppercase: ")
num_string = ""


for char in stringentered:
    num_string += str(ord(char)-23)

print(num_string)


stringentered = ""

for i in range(0,len(num_string)-1,2):
    char_code = num_string [i] + num_string [i+1]

    stringentered += chr(int(char_code)+23)

print(stringentered)




