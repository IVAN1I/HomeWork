def longest_words(file):
    with open(file, 'r', encoding='utf8') as f:
        text = f.read()

    words = text.split()
    max_lenght = max(len(word)for word in words)
    resoult = [word for word in words if len(word) == max_lenght]
    return resoult


resoult = longest_words("article.txt")
print(resoult)

