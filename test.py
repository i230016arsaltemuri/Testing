def print_diamond(n):
    # n should be odd for a symmetric diamond
    if n % 2 == 0:
        n += 1
    for i in range(n):
        spaces = abs(n // 2 - i)
        stars = n - 2 * spaces
        print(" " * spaces + "*" * stars)
    print("")  # Print a newline at the end

print("Diamond pattern of size 7:")

# Example usage:
print_diamond(7)
