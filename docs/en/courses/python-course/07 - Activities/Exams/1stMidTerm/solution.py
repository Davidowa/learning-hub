import random


def exercise2() -> None:
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    guesses = 0

    print("Guess the number (between 1 and 100):")

    while True:
        guess = int(input())
        guesses += 1

        if guess < number_to_guess:
            print("Too low, try again.")
        elif guess > number_to_guess:
            print("Too high, try again.")
        else:
            print(f"Congratulations! You've guessed the right number in {
                  guesses} guesses.")
            break


def exercise3() -> None:
    # Ask the user how many words will be entered
    num_words = int(input("How many words will you enter? "))

    # Initialize a list to store the words
    words = []

    # Prompt the user to enter the specified number of words
    for i in range(num_words):
        word = input("Enter a word: ")
        words.append(word)

    # Calculate the frequency of each word manually
    word_frequency = {}

    for word in words:
        found = False  # Flag to track if the word is found in the dictionary keys
        for key in word_frequency.keys():
            if word == key:
                word_frequency[word] += 1
                found = True
                break
        if not found:
            word_frequency[word] = 1

    # Find the unique words
    unique_words = set(words)

    # Initialize variables to track the longest and shortest word lengths
    longest_word_length = 0
    shortest_word_length = 10000  # Use 'inf' for an initially "infinite" length

    # Initialize lists to hold the longest and shortest words
    longest_words = []
    shortest_words = []

    # Loop through each word to find the longest and shortest word lengths
    for word in unique_words:
        word_length = len(word)
        if word_length > longest_word_length:
            longest_word_length = word_length
        if word_length < shortest_word_length:
            shortest_word_length = word_length

    # Now that we have the lengths, find the words that match
    for word in unique_words:
        if len(word) == longest_word_length:
            longest_words.append(word)
        if len(word) == shortest_word_length:
            shortest_words.append(word)

    # Display the total number of words and the number of unique words
    print(f"Total number of words: {len(words)}")
    print(f"Number of unique words: {len(unique_words)}")

    # Display the frequency of each word
    print("\nWord Frequencies:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

    # Display the longest word(s)
    print("\nLongest word(s):")
    for word in longest_words:
        print(word)

    # Display the shortest word(s)
    print("\nShortest word(s):")
    for word in shortest_words:
        print(word)

    # Display words in alphabetical order
    print("\nWords in alphabetical order:")
    for word in sorted(unique_words):
        print(word)
