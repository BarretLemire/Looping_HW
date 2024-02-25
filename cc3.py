def char_count_foreach(target: str, c: str):
    count = 0
    for char in target:
        if char == c:
            count += 1
    return count

target = "hello world"
c = "o"
result = char_count_foreach(target, c)
print(f"The character '{c}' appears {result} times in the target string.")
