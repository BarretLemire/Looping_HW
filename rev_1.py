def reverse_while(s):
    reversed_string = ""

    while len(s) > 0:
        last_char = s[-1] 
        reversed_string += last_char
        s = s[:-1]
    return reversed_string

