# Lets say we have some text.
# We want to know the most repeated character in the text.

# Example:
sentence = "This is a common interview question"

# Output:
# Most repeated character:  o

# Note: You should ignore the case. So, 'O' and 'o' are the same character.
# Hint: Use the function "max" and "count".

# Solution:
sentence = "This is a common interview question"
sentence = sentence.lower()
print(sentence)  # this is a common interview question
max_char = max(sentence, key=sentence.count)  # i
print(max_char)  # i

# Explanation:
# The function "max" returns the maximum value of a list.
# The function "count" returns the number of times a value appears in a list.
# The function "max" receives a list as parameter.
# The function "count" receives a value as parameter.
# The function "max" returns the value that appears the most times in the list.


# Another solution is to use a dictionary and a for loop.
sentence = "This is a common interview question"
sentence = sentence.lower()
print(sentence)  # this is a common interview question
char_count = {}
for char in sentence:
    char_count[char] = sentence.count(char)
# {'t': 4, 'h': 2, 'i': 5, 's': 3, ' ': 5, 'a': 1, 'c': 1, 'o': 3, 'm': 2, 'n': 3, 'v': 1, 'e': 2, 'r': 1, 'q': 1, 'u': 1}
print(char_count)
max_char = max(char_count, key=char_count.get)  # i
print(max_char)  # i

# Explanation:
# The variable "char_count" is a dictionary.
# The variable "char_count" has the characters of the sentence as keys.
# The variable "char_count" has the number of times each character appears as values.
# The function "max" returns the maximum value of a list.
# The function "get" returns the value of a key in a dictionary.
# The function "max" receives a list as parameter.
# The function "get" receives a key as parameter.
# The function "max" returns the key that has the maximum value in the list.


# Another solution is to use a dictionary and a for loop.

sentence = "This is a common interview question"
sentence = sentence.lower()
print(sentence)  # this is a common interview question
char_count = {}
for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
# {'t': 4, 'h': 2, 'i': 5, 's': 3, ' ': 5, 'a': 1, 'c': 1, 'o': 3, 'm': 2, 'n': 3, 'v': 1, 'e': 2, 'r': 1, 'q': 1, 'u': 1}

sorted_char_count = sorted(
    char_count.items(), key=lambda kv: kv[1], reverse=True)
# [('i', 5), (' ', 5), ('t', 4), ('s', 3), ('o', 3), ('n', 3), ('h', 2), ('m', 2), ('e', 2), ('a', 1), ('c', 1), ('v', 1), ('r', 1), ('q', 1), ('u', 1)]
print(sorted_char_count)
max_char = sorted_char_count[0][0]  # i
print(max_char)  # i

# Explanation:
# The variable "char_count" is a dictionary.
# The variable "char_count" has the characters of the sentence as keys.
# The variable "char_count" has the number of times each character appears as values.
# The function "sorted" returns a sorted list.
# The function "items" returns a list of tuples.
# The function "lambda" is an anonymous function.
# The function "lambda" receives a tuple as parameter.
# The function "lambda" returns the second element of the tuple.
# The function "sorted" receives a list as parameter.
# The function "sorted" returns a sorted list.
# The function "sorted" sorts the list in ascending order by default.
# The function "sorted" sorts the list in descending order if the parameter "reverse" is True.
# The function "sorted" sorts the list by the second element of each tuple.
# The function "sorted" returns the list in descending order.
# The variable "max_char" is the first element of the first tuple in the list.
# The first element of the tuple is the character.
# The second element of the tuple is the number of times the character appears.
# The variable "max_char" is the character that appears the most times in the sentence.
