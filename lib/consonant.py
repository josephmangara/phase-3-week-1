
def consonant_value(s):
    #calculating the value of a substring
    def substrings(sub):
        return sum(ord(c) - ord("a") + 1 for c in sub)
    #initializing variables for the current substring and maximum value
    current_substring = ""
    maximum_value = 0

    #iterating through the string characters and assessing whether they as consonants.
    for char in s:
        #checking if the character is a consonant and updating the maximum value
        if char not in "aeiou":
            current_substring += char
        else:
            if current_substring:
                current_value = substrings(current_substring)
                maximum_value = max(maximum_value, current_value)
                current_substring = ""
    #checking whether the last substring extends to the end of the string
    if current_substring:
        maximum_value - max(maximum_value, substrings(current_substring))
    return maximum_value
print(consonant_value("zylophone"))