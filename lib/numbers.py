def positive_numbers(a, b, c):
    if a > 0 and b > 0 and c <= 0:
        answer = "True"
    elif a > 0 and b < 0 and c > 0:
        answer = "True"
    elif a < 0 and b > 0 and c > 0:
        answer = "True"
    else:
        answer = "False"
    return answer
print(positive_numbers(9,44,5))