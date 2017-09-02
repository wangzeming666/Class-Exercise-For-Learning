line1 = "hello tarena!"
line2 = "my name is weimingze"
line3 = "good-bye"
space = ' '
space1 = len(line2) - len(line1)
space11 = space1 // 2 + 1
space12 = space1 - space11 + 2
space2 = 1
space3 = len(line2) - len(line3)
space31 = space3 // 2 + 1
space32 = space3 - space31 + 2
heng1 = len(line2) + 2
print("+" + "-" * heng1 + "+")
print("|" + space * heng1 + "|")
print("|" + space * space11 + line1 + space * space12 + "|")
print("|" + space * space2 + line2 + space * space2 + "|")
print("|" + space * space31 + line3 + space * space32 + "|")
print("|" + space * heng1 + "|")
print("+" + "-" * heng1 + "+")
