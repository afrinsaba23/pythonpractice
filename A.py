#remove duplicate words form a string  
def remove_duplicate_words(input_string):
    words = input_string.split()
    unique_words = list(dict.fromkeys(words))
    return ' '.join(unique_words)

input_string = "This is is a test test string string"
result = remove_duplicate_words(input_string)
print(result)
# Output: "This is a test string"
x=420
print(x)
