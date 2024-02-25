def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    result = []
    for i in range(len(a)):
        result.append(a[i] * b[i])
    return result

