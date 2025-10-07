def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        return None
    return max(numbers)

def is_palindrome(text):
    """Check if a string is a palindrome."""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4, 5]
    print(f"Sum: {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Max: {find_max(numbers)}")
    print(f"Is 'radar' a palindrome? {is_palindrome('radar')}")