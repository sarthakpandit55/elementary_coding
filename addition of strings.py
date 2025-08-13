def addNumberStrings(input1, input2):
    if len(input1) < len(input2):
        input1, input2 = input2, input1

    result = []
    carry = 0

    s1 = input1[::-1]
    s2 = input2[::-1]

    for i in range(len(s1)):
        digit1 = int(s1[i])
        digit2 = int(s2[i]) if i < len(s2) else 0

        current_sum = digit1 + digit2 + carry

        result.append(str(current_sum % 10))

        carry = current_sum // 10

    if carry > 0:
        result.append(str(carry))

    return "".join(result[::-1])


addNumberStrings("1234", "56")