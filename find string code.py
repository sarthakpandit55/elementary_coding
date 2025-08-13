def process_string(input1: str) -> int:
    words = input1.split(" ")
    result = ""

    for word in words:
        word = word.upper()
        left, right = 0, len(word) - 1
        total_sum = 0

        while left < right:
            left_val = ord(word[left]) - ord('A') + 1
            right_val = ord(word[right]) - ord('A') + 1
            total_sum += abs(left_val - right_val)
            left += 1
            right -= 1

        # If odd length, add middle letter's value
        if left == right:
            total_sum += ord(word[left]) - ord('A') + 1

        result += str(total_sum)

    return int(result)
print(process_string("ABC XYZ"))