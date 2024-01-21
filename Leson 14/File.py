handle = open("write_file.txt", mode='w')
while True:
    some_text = input("Write:")
    if not some_text:
        break
    handle.write('\n'+some_text)
handle.close()

