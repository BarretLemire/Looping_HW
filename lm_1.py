def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    result = []
    i = 0
    while i > len(a):
        result.append(a[i] * b[i])
        i += 1
    return result

