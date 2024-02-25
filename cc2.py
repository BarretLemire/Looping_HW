def char_count_for(target: str, c: str):
    count = 0
    for char in target:
        if char == c:
            count += 1
    return count

# Example usage:
target = "hello world"
c = "o"
result = char_count_for(target, c)
print(f"The character '{c}' appears {result} times in the target string.")
    
