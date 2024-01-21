def update_hero(**kwargs):
    with open('hero.ini', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        key, value = line.strip().split('=')
        if key in kwargs:
            lines[i] = f"{key}={kwargs[key]}\n"

    with open('hero.ini', 'w') as file:
        file.writelines(lines)

update_hero(hero="Halk", power=450, Y=2.3)

