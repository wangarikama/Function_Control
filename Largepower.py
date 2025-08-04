def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False

print(large_power(2, 13))  # Example usage
print(large_power(3, 8))   # Another example