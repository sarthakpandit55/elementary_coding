def getCodeThroughStrings(input1) :
    words = input1.split(" ")
    total_length = sum(len(word) for word in words)

    while total_length > 9:
        total_length = sum(int(digit) for digit in str(total_length))

    return total_length