# Challenge is decrypt a working decryption scheme
# Take each number in message mod 37 and map it to the follwing character set
# 0-25 = alphabet in uppercase
# 26-35 = decimals 0-9
# 36 = underscore
# Wrap your decrypted message in format: picoCTF{decrypted_message}

#!/usr/bin/python3
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
numbers = [165,248,94,346,299,73,198,221,313,137,205,87,336,110,186,69,223,213,216,216,177,138]
print("picoCTF{", end="")

for number in numbers:
    remainder = number % 37

    if 0 <= remainder <= 36:
        print(characters[remainder], end="")
print("}")
