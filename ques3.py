import re

# Original text
text = """I’m fascinated by the world of technology. Every day, new innovations like artificial intelligence, robotics, and quantum computing are reshaping our lives. Technology makes communication faster, knowledge more accessible, and businesses more efficient. I love learning about cutting-edge gadgets, smart home devices, and software that simplify daily tasks. The future of technology excites me because it holds endless possibilities for creativity and problem-solving."""

# 2a. Extract all words with more than 5 letters
more_than_5_letters = re.findall(r'\b[a-zA-Z]{6,}\b', text)

# 2b. Extract all numbers (if any)
numbers = re.findall(r'\b\d+\b', text)

# 2c. Extract all capitalized words
capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', text)

# 3a. Split text into words containing only alphabets
only_alphabets = re.findall(r'\b[a-zA-Z]+\b', text)

# 3b. Extract words starting with a vowel
words_starting_with_vowel = [word for word in only_alphabets if re.match(r'^[aeiouAEIOU]', word)]

# Displaying the results
print("Words with more than 5 letters:\n", more_than_5_letters)
print("\nNumbers in the text:\n", numbers)
print("\nCapitalized Words:\n", capitalized_words)
print("\nWords containing only alphabets:\n", only_alphabets)
print("\nWords starting with a vowel:\n", words_starting_with_vowel)
