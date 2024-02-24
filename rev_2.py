def reverse_for(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string



#test
test_strings = ["axe" , "wood"]

for test_string in test_strings:
    reversed_string = reverse_for(test_string)
    print(f"Original: {test_string}, Reversed: {reversed_string}")


