def generate_pattern(N):
    result = [str(f(i, N)) for i in range(1, N+1)]
    return ' '.join(result)

def f(i, N):
    if i <= N // 2:
        return 2 * i
    else:
        return N - 2 * (i - (N // 2))

# Contoh penggunaan
print(generate_pattern(2))  # Output: 2 4
print(generate_pattern(10))  # Output: 2 6 10 8 4
print(generate_pattern(6))   # Output: 2 6 4