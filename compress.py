def compress(input):
    if len(input) == 0:
        return ""

    count = 1
    output = ""
    for i in range(len(input)):
        # If end of string
        if i == len(input) - 1:
            output += input[i]
            if count > 1:
                output += str(count)
        # If next char is same as current char
        elif input[i] == input[i+1]:
            count += 1
        # If next char is different from current char
        else:
            output += input[i]
            if count > 1:
                output += str(count)
            count = 1

    return output


print(compress("AAABBBAADDdBBCCC"))
print(compress("ABC"))
print(compress("A"))
print(compress(""))
