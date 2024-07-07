import string
import random
x1=list(string.ascii_lowercase)
x2=list(string.ascii_uppercase)
x3=list(string.digits)
x4=list(string.punctuation)
user_input = input(" How many characters do you want in password? ")
while True:
    try:
        characters_number = int(user_input)
        if characters_number < 7:
            print("Your number should be at least 7.")
            user_input = input("Please,Enter your number again:")
        else:
            break
    except:
        print("please, Enter numbers only.")
        user_input = input(" How many characters do you want in password? ")
random.shuffle(x1)
random.shuffle(x2)
random.shuffle(x3)
random.shuffle(x4)
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))
result = []
for x in range (part1):
    result.append(x1[x])
    result.append(x2[x])
for x in range (part2):
    result.append(x3[x])
    result.append(x4[x])
random.shuffle(result)
password = "".join(result)
print("Strong Password:", password)
        
        
        
