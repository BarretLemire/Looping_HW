def reverse_foreach(s):

    index = len(s) - 1
    while index >= 0:
        print(s[index], end="")
        index -= 1
    print() 

s = "Hello, World!"
reverse_foreach(s)

