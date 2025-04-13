import re

# Original Text
text = """I’m fascinated by the world of technology. Every day, new innovations like artificial intelligence, robotics, and quantum computing are reshaping our lives. Technology makes communication faster, knowledge more accessible, and businesses more efficient. I love learning about cutting-edge gadgets, smart home devices, and software that simplify daily tasks. The future of technology excites me because it holds endless possibilities for creativity and problem-solving."""

# 2. Custom Tokenization Function
def custom_tokenizer(text):
    # Keep contractions, hyphenated words, and decimal numbers
    pattern = r"\b\w+(?:[-']\w+)*\.?\w*\b|\d+\.\d+"
    tokens = re.findall(pattern, text)
    return tokens

# Apply custom tokenizer
tokens = custom_tokenizer(text)

# 3. Regex Substitutions

# Example string with fake emails, URLs, and phone numbers
text_with_examples = """You can contact me at john.doe@example.com or visit https://www.example.com for details.
Call me at 123-456-7890 or +91 9876543210."""

# a. Replace email addresses
cleaned_text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '<EMAIL>', text_with_examples)

# b. Replace URLs
cleaned_text = re.sub(r'https?://\S+|www\.\S+', '<URL>', cleaned_text)

# c. Replace phone numbers
cleaned_text = re.sub(r'(\+?\d{1,3}[\s-]?\d{10}|\d{3}-\d{3}-\d{4})', '<PHONE>', cleaned_text)

# Display Results
print("Custom Tokenized Output:\n", tokens)
print("\nCleaned Text with Placeholders:\n", cleaned_text)
