text = """Любіть Україну, як сонце, любіть,
як вітер, і трави, і води…
В годину щасливу і в радості мить,
любіть у годину негоди.
Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов’їну.
Між братніх народів, мов садом рясним,
сіяє вона над віками…
Любіть Україну всім серцем своїм
і всіми своїми ділами.
Для нас вона в світі єдина, одна
в просторів солодкому чарі…
Вона у зірках, і у вербах вона,
і в кожному серця ударі,
у квітці, в пташині, в електровогнях,
у пісні у кожній, у думі,
в дитячий усмішці, в дівочих очах
і в стягів багряному шумі…"""

cleaned_text = ''.join(c.lower() if c.isalpha() or c.isspace() else ' ' for c in text)

words = cleaned_text.split()

word_count = {}
for word in words :
    if word in word_count :
        word_count[word] += 1
    else :
        word_count[word] = 1

max_word = max(word_count , key=word_count.get)
min_word = min(word_count , key=word_count.get)

print("Встречается больше раз:", max_word, word_count[max_word])
print("Встречается меньше раз:", min_word, word_count[min_word])
