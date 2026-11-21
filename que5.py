def count_frequencies(text):
    clean_text = text.lower()

    words = clean_text.split()
    word_count = {}

    for word in words:
        word = word.strip(".,!?;:\"'()")
        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    char_count = {}

    for char in clean_text:
        if char != " ":
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return word_count, char_count

sample_text = input("Enter a text string: ")

words_freq, chars_freq = count_frequencies(sample_text)

print("\n--- Word Frequencies ---")
for word, count in words_freq.items():
    print(f"'{word}': {count}")

print("\n--- Character Frequencies ---")
for char, count in chars_freq.items():
    print(f"'{char}': {count}")
