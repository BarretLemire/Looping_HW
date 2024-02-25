def char_count_while(target: str, c: str):
    count = 0
    i = 0
    while i < len(target):
        if target[i] == c:
            count += 1
        i += 1
    return count


target = "hello world"
c = "o"
result = char_count_while(target, c)
print(f" '{c}' appears in '{target}' {result} times.")

