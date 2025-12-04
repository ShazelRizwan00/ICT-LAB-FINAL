def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = 13
print(f"{num} is {check_even_or_odd(num)}")
