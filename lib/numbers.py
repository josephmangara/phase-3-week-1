def positive_numbers(a, b, c):
    if (a == "+" and b == "+") and c == "-":
        answer = "True"
    elif a == "+" and b == "-" and c == "+":
        answer = "True"
    elif a == "-" and b == "+" and c == "+":
        answer = "True"
    else:
        answer = "False"
    return answer
print(positive_numbers(9,44,-2))