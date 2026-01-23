name = input().strip()
unique = len(set(name))

if unique % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
