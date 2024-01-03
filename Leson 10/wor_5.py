text = 'Python is good language to learn and in same time we like to tell that it is cool expereance for us'

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else :
        char_count[char] = 1

print(char_count)

